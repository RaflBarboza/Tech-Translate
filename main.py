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

        # Botão para abrir a janela de lição
        self.lesson_button = tk.Button(self.frame, text="Lição", command=self.show_lesson)
        self.lesson_button.pack(side=tk.LEFT, padx=5)

        # Tamanho da janela principal
        self.root.geometry("400x200")

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
        supported_languages = {
            'af': 'Africâner', 'sq': 'Albanês', 'am': 'Amárico', 'ar': 'Árabe', 'hy': 'Armênio',
            'az': 'Azerbaijano', 'eu': 'Basco', 'be': 'Bielorrusso', 'bn': 'Bengali', 'bs': 'Bósnio',
            'bg': 'Búlgaro', 'ca': 'Catalão', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinês (Simplificado)',
            'zh-tw': 'Chinês (Tradicional)', 'co': 'Córsico', 'hr': 'Croata', 'cs': 'Tcheco', 'da': 'Dinamarquês',
            'nl': 'Holandês', 'en': 'Inglês', 'eo': 'Esperanto', 'et': 'Estoniano', 'fil': 'Filipino', 'fi': 'Finlandês',
            'fr': 'Francês', 'fy': 'Frísio', 'gl': 'Galês', 'ka': 'Georgiano', 'de': 'Alemão', 'el': 'Grego',
            'gu': 'Guzerate', 'ht': 'Haitiano', 'ha': 'Hauçá', 'haw': 'Havaiano', 'iw': 'Hebraico', 'hi': 'Hindi',
            'hmn': 'Hmong', 'hu': 'Húngaro', 'is': 'Islandês', 'ig': 'Igbo', 'id': 'Indonésio', 'ga': 'Irlandês',
            'it': 'Italiano', 'ja': 'Japonês', 'jw': 'Javanês', 'kn': 'Canarês', 'kk': 'Cazaque', 'km': 'Khmer',
            'rw': 'Kinyarwanda', 'ko': 'Coreano', 'ku': 'Curdo (Kurmanji)', 'ky': 'Quirguiz', 'lo': 'Lao',
            'la': 'Latim', 'lv': 'Letão', 'lt': 'Lituano', 'lb': 'Luxemburguês', 'mk': 'Macedônio',
            'mg': 'Malgaxe', 'ms': 'Malaio', 'ml': 'Malaiala', 'mt': 'Maltês', 'mi': 'Maori', 'mr': 'Marata',
            'mn': 'Mongol', 'my': 'Birmanês', 'ne': 'Nepalês', 'no': 'Norueguês', 'or': 'Odia',
            'ps': 'Pashto', 'fa': 'Persa', 'pl': 'Polonês', 'pt': 'Português', 'pa': 'Punjabi', 'ro': 'Romeno',
            'ru': 'Russo', 'sm': 'Samoano', 'gd': 'Gaélico Escocês', 'sr': 'Sérvio', 'st': 'Soto', 'sn': 'Shona',
            'sd': 'Sindi', 'si': 'Cingalês', 'sk': 'Eslovaco', 'sl': 'Esloveno', 'so': 'Somali', 'es': 'Espanhol',
            'su': 'Sundanês', 'sw': 'Suaíli', 'sv': 'Sueco', 'tg': 'Tajique', 'ta': 'Tâmil', 'te': 'Telugu',
            'th': 'Tailandês', 'tr': 'Turco', 'uk': 'Ucraniano', 'ur': 'Urdu', 'ug': 'Uigur', 'uz': 'Usbeque',
            'vi': 'Vietnamita', 'cy': 'Galês', 'xh': 'Xhosa', 'yi': 'Iídiche', 'yo': 'Iorubá', 'zu': 'Zulu'
        }

        self.lang_window = tk.Toplevel(self.root)
        self.lang_window.title("Selecionar Idioma")

        label_lang = tk.Label(self.lang_window, text="Selecione o Idioma Alvo:")
        label_lang.pack(pady=10)

        self.listbox = tk.Listbox(self.lang_window, selectmode=tk.SINGLE, width=40, height=15)
        self.listbox.pack(pady=5)

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
        """Verifica se a tradução inserida está correta."""
        user_answer = self.answer_entry.get().strip().lower()
        if user_answer == translated_sentence.lower():
            messagebox.showinfo("Resposta Correta", "Parabéns! Sua tradução está correta.")
        else:
            messagebox.showwarning("Resposta Incorreta", f"Sua tradução está incorreta. A tradução correta de\n\n'{original_sentence}'\n\né:\n\n'{translated_sentence}'.")

    def show_lesson(self):
        """Mostra uma lição com botões de idiomas."""
        self.lesson_window = tk.Toplevel(self.root)
        self.lesson_window.title("Lição")

        label = tk.Label(self.lesson_window, text="Selecione um idioma para ver a lição:", pady=10)
        label.pack()

        button_frame = tk.Frame(self.lesson_window)
        button_frame.pack(pady=10)

        # Botões para os principais idiomas
        languages = ["Inglês", "Espanhol", "Francês", "Alemão", "Italiano"]
        for lang in languages:
            button = tk.Button(button_frame, text=lang, command=lambda l=lang: self.show_lesson_content(l))
            button.pack(side=tk.LEFT, padx=5)

    def show_lesson_content(self, language):
        """Mostra o conteúdo da lição para o idioma selecionado."""
        lessons = {
            "Inglês": """
            Bem-vindo à lição de Inglês!
            - Hello: Olá
            - Thank you: Obrigado
            - Please: Por favor
            - Yes: Sim
            - No: Não
            """,
            "Espanhol": """
            Bienvenido a la lección de Español!
            - Hola: Olá
            - Gracias: Obrigado
            - Por favor: Por favor
            - Sí: Sim
            - No: Não
            """,
            "Francês": """
            Bienvenue à la leçon de Français!
            - Bonjour: Olá
            - Merci: Obrigado
            - S'il vous plaît: Por favor
            - Oui: Sim
            - Non: Não
            """,
            "Alemão": """
            Willkommen zur Deutschlektion!
            - Hallo: Olá
            - Danke: Obrigado
            - Bitte: Por favor
            - Ja: Sim
            - Nein: Não
            """,
            "Italiano": """
            Benvenuto alla lezione di Italiano!
            - Ciao: Olá
            - Grazie: Obrigado
            - Per favore: Por favor
            - Sì: Sim
            - No: Não
            """
        }

        if language in lessons:
            lesson_content = lessons[language]
            lesson_window = tk.Toplevel(self.root)
            lesson_window.title(f"Lição de {language}")

            label_lesson = tk.Label(lesson_window, text=lesson_content, justify=tk.LEFT, padx=10, pady=10)
            label_lesson.pack()

            exercise_button = tk.Button(lesson_window, text="Exercício", command=lambda: self.show_lesson_exercise(language))
            exercise_button.pack(pady=10)

    def show_lesson_exercise(self, language):
        """Mostra um exercício para o idioma selecionado."""
        exercises = {
            "Inglês": [
                ("Hello, ___ are you?", "how"),
                ("Thank you very ___", "much"),
                ("Please, ___ me the book.", "give"),
                ("Yes, I ___ understand.", "can"),
                ("No, I do ___ want it.", "not")
            ],
            "Espanhol": [
                ("Hola, ¿___ estás?", "cómo"),
                ("Gracias ___ todo.", "por"),
                ("Por favor, ___ me el libro.", "dame"),
                ("Sí, yo ___ entiendo.", "puedo"),
                ("No, no ___ lo quiero.", "lo")
            ],
            "Francês": [
                ("Bonjour, comment ___?", "ça va"),
                ("Merci ___ tout.", "pour"),
                ("S'il vous plaît, ___ moi le livre.", "donnez"),
                ("Oui, je ___ comprendre.", "peux"),
                ("Non, je ne ___ veux pas.", "le")
            ],
            "Alemão": [
                ("Hallo, wie ___?", "geht's"),
                ("Danke ___ alles.", "für"),
                ("Bitte, ___ mir das Buch.", "geben"),
                ("Ja, ich ___ verstehen.", "kann"),
                ("Nein, ich will ___.", "nicht")
            ],
            "Italiano": [
                ("Ciao, come ___?", "stai"),
                ("Grazie ___ tutto.", "per"),
                ("Per favore, ___ il libro.", "dammi"),
                ("Sì, io ___ capire.", "posso"),
                ("No, non ___ voglio.", "lo")
            ]
        }

        if language in exercises:
            exercise, answer = random.choice(exercises[language])
            exercise_window = tk.Toplevel(self.root)
            exercise_window.title(f"Exercício de {language}")

            label_exercise = tk.Label(exercise_window, text=exercise, padx=10, pady=10)
            label_exercise.pack()

            self.answer_entry = tk.Entry(exercise_window, width=50)
            self.answer_entry.pack(pady=5)

            check_button = tk.Button(exercise_window, text="Verificar", command=lambda: self.check_lesson_exercise(answer))
            check_button.pack(pady=5)

    def check_lesson_exercise(self, correct_answer):
        """Verifica se a resposta do exercício está correta."""
        user_answer = self.answer_entry.get().strip().lower()
        if user_answer == correct_answer:
            messagebox.showinfo("Resposta Correta", "Parabéns! Sua resposta está correta.")
        else:
            messagebox.showwarning("Resposta Incorreta", f"Sua resposta está incorreta. A resposta correta é '{correct_answer}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
