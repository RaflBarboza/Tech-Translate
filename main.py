import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator
import random

class TranslatorApp:
    def __init__(self, root):
        """Inicia a aplicação do tradutor."""
        self.root = root
        self.root.title("Tech Translate")

        # Cria um frame principal para os botões
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

        # Botão para abrir a janela de tradução
        self.translate_button = tk.Button(self.frame, text="Abrir Tradutor", command=self.open_translation_window)
        self.translate_button.pack(side=tk.LEFT, padx=5)

        # Botão para iniciar os exercícios
        self.exercise_button = tk.Button(self.frame, text="Exercícios", command=self.show_random_translation_exercise)
        self.exercise_button.pack(side=tk.LEFT, padx=5)

        # Tamanho da janela principal
        self.root.geometry("300x150")

    def open_translation_window(self):
        """Abre a janela de tradução."""
        self.translation_window = tk.Toplevel(self.root)
        self.translation_window.title("Resultado da Tradução")

        # Criação das coisas da janela de tradução
        self.label_result = tk.Label(self.translation_window, text="Resultado da Tradução")
        self.label_result.pack(pady=10)

        self.input_text = tk.Text(self.translation_window, height=5, width=50)
        self.input_text.pack(pady=5)

        self.translate_button = tk.Button(self.translation_window, text="Traduzir", command=self.translate_text)
        self.translate_button.pack(pady=5)

        self.output_text = tk.Text(self.translation_window, height=5, width=50)
        self.output_text.pack(pady=5)

        # Criação do botão para selecionar o idioma
        self.language_frame = tk.Frame(self.translation_window)
        self.language_frame.pack(pady=10)
        self.language_button = tk.Button(self.language_frame, text="Selecionar Idioma", command=self.show_language_options)
        self.language_button.pack(pady=5)

    def translate_text(self):
        """Traduz o texto de entrada para o idioma."""
        text_to_translate = self.input_text.get("1.0", "end-1c")
        target_lang = getattr(self, 'target_language', 'en')  # Idioma alvo (padrão: inglês)
        translator = GoogleTranslator(source="pt", target=target_lang)
        try:
            translated_text = translator.translate(text_to_translate)
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", translated_text)
        except Exception as e:
            messagebox.showerror("Erro de Tradução", f"Ocorreu um erro ao traduzir: {str(e)}")

    def show_language_options(self):
        """Mostra uma janela com opções de idiomas."""
        supported_languages = {
            # Dicionário de idiomas suportados
        }

        # Cria a janela para selecionar o idioma
        self.lang_window = tk.Toplevel(self.root)
        self.lang_window.title("Selecionar Idioma")

        label_lang = tk.Label(self.lang_window, text="Selecione o Idioma Alvo:")
        label_lang.pack(pady=10)

        self.listbox = tk.Listbox(self.lang_window, selectmode=tk.SINGLE, width=40, height=15)
        self.listbox.pack(pady=5)

        # Lista com os idiomas disponíveis
        for lang_code, lang_name in supported_languages.items():
            self.listbox.insert(tk.END, f"{lang_name} ({lang_code})")

        confirm_button = tk.Button(self.lang_window, text="Confirmar", command=self.set_language)
        confirm_button.pack(pady=10)

    def set_language(self):
        """Define o idioma selecionado."""
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index)
            lang_code = selected_item.split('(')[-1].strip(')').strip()
            self.target_language = lang_code
            self.lang_window.destroy()
        else:
            messagebox.showwarning("Selecione um Idioma", "Por favor, selecione um idioma.")

    def show_random_translation_exercise(self):
        """Mostra um exercício de tradução com uma frase aleatória em inglês."""
        if hasattr(self, 'target_language'):
            target_lang = self.target_language
        else:
            target_lang = 'pt'  # Define o idioma padrão como português

        # Frases para os exercícios de tradução em inglês e outros idiomas
        sentences = {
            'en': ['Hello, how are you?', 'What is your name?', 'Where are you from?', 'I like programming.'],
            'es': ['Hola, ¿cómo estás?', '¿Cuál es tu nombre?', '¿De dónde eres?', 'Me gusta programar.'],
            'fr': ['Bonjour, comment ça va?', 'Comment tu t\'appelles?', 'D\'où viens-tu?', 'J\'aime programmer.']
            # Colocar mais frases para outros idiomas se quiser.
        }

        random_sentence = random.choice(sentences['en'])  # Escolhe uma frase aleatória em inglês
        translator = GoogleTranslator(source='en', target=target_lang)
        translated_sentence = translator.translate(random_sentence)

        # Cria a janela do exercício de tradução
        self.exercise_window = tk.Toplevel(self.root)
        self.exercise_window.title("Exercício de Tradução")

        label_sentence = tk.Label(self.exercise_window, text=random_sentence)
        label_sentence.pack(pady=10)

        self.answer_entry = tk.Entry(self.exercise_window, width=50)
        self.answer_entry.pack(pady=5)

        check_button = tk.Button(self.exercise_window, text="Verificar", command=lambda: self.check_translation(random_sentence, translated_sentence))
        check_button.pack(pady=5)

    def check_translation(self, original_sentence, translated_sentence):
        """Verifica se a tradução inserida pelo usuário está correta."""
        user_answer = self.answer_entry.get().strip().lower()
        if user_answer == translated_sentence.lower():
            messagebox.showinfo("Resposta Correta", "Parabéns! Sua tradução está correta.")
        else:
            messagebox.showwarning("Resposta Incorreta", f"Sua tradução está incorreta. A tradução correta de\n\n'{original_sentence}'\n\né:\n\n'{translated_sentence}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()