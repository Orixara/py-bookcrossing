from django import forms

from books.models import Author, BookListing


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    author_new = forms.CharField(
        required=False,
        label="New Author",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter author's full name"})
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = BookListing
        fields = [
            "title",
            "author",
            "author_new",
            "genre",
            "image",
            "condition",
            "description"
        ]

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get("author")
        author_new = cleaned_data.get("author_new")

        if author and author_new:
            raise forms.ValidationError("Choose author or create new one, but not both options.")

        if not author and not author_new:
            raise forms.ValidationError("Specify the author — select an existing one or add a new one.")

        if author_new:
            normalized = author_new.strip().title()
            existing = Author.objects.filter(full_name__iexact=normalized).first()
            if existing:
                cleaned_data["author"] = existing
            else:
                cleaned_data["author"], _ = Author.objects.get_or_create(full_name=normalized)

        return cleaned_data