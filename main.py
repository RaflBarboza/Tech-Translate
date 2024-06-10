import tkinter as tk
from tkinter import messagebox, ttk
from deep_translator import GoogleTranslator
import random
import webbrowser

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

        # Botão para acompanhar o progresso
        self.progress_button = tk.Button(self.frame, text="Acompanhamento de Progresso", command=self.show_progress)
        self.progress_button.pack(side=tk.LEFT, padx=5)

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
            'fr': ['Bonjour, comment ça va?', 'Comment tu t\'appelles?', 'D\'où viens-tu?', 'J\'aime programmer.'],
            'de': ['Hallo, wie geht\'s?', 'Wie heißt du?', 'Woher kommst du?', 'Ich mag programmieren.'],
        }

        self.exercise_window = tk.Toplevel(self.root)
        self.exercise_window.title("Exercício de Tradução")

        random_sentence = random.choice(sentences['en'])
        translated_sentence = GoogleTranslator(source='en', target=target_lang).translate(random_sentence)

        self.label_exercise = tk.Label(self.exercise_window, text=f"Traduza a seguinte frase para {target_lang}:")
        self.label_exercise.pack(pady=10)

        self.label_sentence = tk.Label(self.exercise_window, text=random_sentence)
        self.label_sentence.pack(pady=5)

        self.input_translation = tk.Entry(self.exercise_window, width=50)
        self.input_translation.pack(pady=5)

        self.submit_button = tk.Button(self.exercise_window, text="Enviar", command=lambda: self.check_translation(random_sentence, target_lang, translated_sentence))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.exercise_window, text="")
        self.result_label.pack(pady=10)

    def check_translation(self, sentence, target_lang, correct_translation):
        """Verifica a tradução do usuário."""
        user_translation = self.input_translation.get()
        correct_translation_lower = correct_translation.lower().strip()
        user_translation_lower = user_translation.lower().strip()

        if user_translation_lower == correct_translation_lower:
            self.result_label.config(text="Correto! Tradução correta.")
        else:
            self.result_label.config(text=f"Incorreto. A tradução correta é: {correct_translation}")

    def show_lesson(self):
        """Mostra uma lição de frases comuns no idioma selecionado."""
        if hasattr(self, 'target_language'):
            target_lang = self.target_language
        else:
            target_lang = 'en'  # Define o idioma padrão como inglês

        # Frases comuns para a lição
        common_phrases = {
            'en': ['Hello', 'Goodbye', 'Thank you', 'Please', 'Yes', 'No', 'Excuse me'],
            'es': ['Hola', 'Adiós', 'Gracias', 'Por favor', 'Sí', 'No', 'Perdón'],
            'fr': ['Bonjour', 'Au revoir', 'Merci', 'S\'il vous plaît', 'Oui', 'Non', 'Excusez-moi'],
            'de': ['Hallo', 'Tschüss', 'Danke', 'Bitte', 'Ja', 'Nein', 'Entschuldigung'],
        }

        self.lesson_window = tk.Toplevel(self.root)
        self.lesson_window.title("Lição")

        self.label_lesson = tk.Label(self.lesson_window, text=f"Frases comuns em {target_lang}:")
        self.label_lesson.pack(pady=10)

        self.phrases_listbox = tk.Listbox(self.lesson_window, selectmode=tk.SINGLE, width=50, height=10)
        self.phrases_listbox.pack(pady=5)

        for phrase in common_phrases.get(target_lang, common_phrases['en']):
            self.phrases_listbox.insert(tk.END, phrase)

        self.exercise_button = tk.Button(self.lesson_window, text="Exercitar", command=self.show_random_translation_exercise)
        self.exercise_button.pack(pady=10)

    def show_progress(self):
        """Mostra a janela de acompanhamento de progresso."""
        self.progress_window = tk.Toplevel(self.root)
        self.progress_window.title("Acompanhamento de Progresso")

        self.progress = 0
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(self.progress)

        self.progress_bar = ttk.Progressbar(self.progress_window, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=10, padx=10, fill=tk.X)

        self.links = [
            ("Aula 1", "Bem-vindo à sua primeira aula de inglês! Nesta introdução, vamos mergulhar no básico deste idioma fascinante e amplamente utilizado em todo o mundo. O inglês é uma língua global, falada por milhões de pessoas em diversos países e culturas. "
                       "É considerado o idioma internacional dos negócios, da tecnologia, da ciência e da comunicação global. "
                       "Nesta lição introdutória, vamos aprender algumas saudações simples, como 'Hello' (Olá) e 'Goodbye' (Adeus), além de algumas expressões comuns para se apresentar, como 'My name is...' (Meu nome é...) e 'Nice to meet you' (Prazer em conhecê-lo)."
                       "Também exploraremos o alfabeto inglês, os números básicos e algumas palavras-chave que você encontrará com frequência ao iniciar sua jornada no aprendizado deste idioma."
                       "Prepare-se para mergulhar em um novo mundo de possibilidades e expandir seus horizontes através do inglês!"),
            (
            "Aula 2", "Nesta aula, vamos aprender algumas saudações e expressões comuns para se apresentar em inglês.\n"
                      "1. Hello! (Olá!) - Uma saudação comum para cumprimentar alguém.\n"
                      "2. Hi! (Oi!) - Outra forma informal de dizer 'Olá'.\n"
                      "3. Good morning! (Bom dia!) - Usado para cumprimentar alguém pela manhã.\n"
                      "4. Good afternoon! (Boa tarde!) - Usado para cumprimentar alguém durante a tarde.\n"
                      "5. Good evening! (Boa noite!) - Usado para cumprimentar alguém à noite.\n"
                      "6. How are you? (Como vai você?) - Uma pergunta comum para perguntar como alguém está.\n"
                      "7. I'm fine, thank you. And you? (Estou bem, obrigado. E você?) - Uma resposta comum para 'How are you?', seguida de uma pergunta de volta.\n"
                      "8. My name is... (Meu nome é...) - Uma frase para se apresentar e dizer seu nome.\n"
                      "9. Nice to meet you! (Prazer em conhecê-lo!) - Uma expressão usada para mostrar satisfação em conhecer alguém.\n"
                      "10. What's your name? (Qual é o seu nome?) - Outra forma de perguntar o nome de alguém."),
            ("Aula 3", "Nesta aula, vamos aprender alguns verbos básicos em inglês.\n"
                       "1. To be (Ser/Estar) - Usado para expressar identidade, estado ou características.\n"
                       "2. To have (Ter) - Usado para expressar posse ou características físicas.\n"
                       "3. To go (Ir) - Usado para expressar movimento em direção a algum lugar.\n"
                       "4. To come (Vir) - Usado para expressar movimento em direção ao local onde a pessoa está.\n"
                       "5. To do (Fazer) - Usado para expressar uma ação ou atividade.\n"
                       "6. To eat (Comer) - Usado para expressar a ação de se alimentar.\n"
                       "7. To drink (Beber) - Usado para expressar a ação de tomar líquidos.\n"
                       "8. To sleep (Dormir) - Usado para expressar a ação de descansar durante o sono.\n"
                       "9. To work (Trabalhar) - Usado para expressar a ação de realizar atividades laborais.\n"
                       "10. To study (Estudar) - Usado para expressar a ação de aprender algo através de estudo."),
            ("Aula 4", "Nesta aula, vamos aprender sobre o Tempo Presente Simples em inglês.\n"
                       "1. I play (Eu jogo) - Usado para descrever ações habituais ou verdades universais na primeira pessoa do singular.\n"
                       "2. You play (Você joga) - Usado para descrever ações habituais ou verdades universais na segunda pessoa do singular.\n"
                       "3. He/She/It plays (Ele/Ela/Jogam) - Usado para descrever ações habituais ou verdades universais na terceira pessoa do singular.\n"
                       "4. We play (Nós jogamos) - Usado para descrever ações habituais ou verdades universais na primeira pessoa do plural.\n"
                       "5. You play (Vocês jogam) - Usado para descrever ações habituais ou verdades universais na segunda pessoa do plural.\n"
                       "6. They play (Eles/Elas jogam) - Usado para descrever ações habituais ou verdades universais na terceira pessoa do plural.\n"
                       "Note que o verbo no tempo presente simples geralmente recebe 's' na terceira pessoa do singular."),
            ("Aula 5", "Nesta aula, vamos aprender sobre o Tempo Passado Simples em inglês.\n"
                       "1. I played (Eu joguei) - Usado para descrever ações completadas no passado na primeira pessoa do singular.\n"
                       "2. You played (Você jogou) - Usado para descrever ações completadas no passado na segunda pessoa do singular.\n"
                       "3. He/She/It played (Ele/Ela/Jogou) - Usado para descrever ações completadas no passado na terceira pessoa do singular.\n"
                       "4. We played (Nós jogamos) - Usado para descrever ações completadas no passado na primeira pessoa do plural.\n"
                       "5. You played (Vocês jogaram) - Usado para descrever ações completadas no passado na segunda pessoa do plural.\n"
                       "6. They played (Eles/Elas jogaram) - Usado para descrever ações completadas no passado na terceira pessoa do plural.\n"
                       "Observe que para a maioria dos verbos regulares, o passado simples é formado adicionando '-ed' ao verbo no infinitivo."),
            ("Aula 6", "Nesta aula, vamos aprender sobre o Tempo Futuro Simples em inglês.\n"
                       "1. I will play (Eu vou jogar) - Usado para descrever ações futuras na primeira pessoa do singular.\n"
                       "2. You will play (Você vai jogar) - Usado para descrever ações futuras na segunda pessoa do singular.\n"
                       "3. He/She/It will play (Ele/Ela vai jogar) - Usado para descrever ações futuras na terceira pessoa do singular.\n"
                       "4. We will play (Nós vamos jogar) - Usado para descrever ações futuras na primeira pessoa do plural.\n"
                       "5. You will play (Vocês vão jogar) - Usado para descrever ações futuras na segunda pessoa do plural.\n"
                       "6. They will play (Eles/Elas vão jogar) - Usado para descrever ações futuras na terceira pessoa do plural.\n"
                       "O tempo futuro simples é geralmente formado adicionando 'will' antes do verbo no infinitivo."),
            ("Aula 7", "Nesta aula, vamos aprender sobre os Pronomes Pessoais em inglês.\n"
                       "1. I (Eu) - Usado para se referir a si mesmo.\n"
                       "2. You (Você) - Usado para se referir à pessoa com quem se está falando.\n"
                       "3. He (Ele) - Usado para se referir a um homem ou menino.\n"
                       "4. She (Ela) - Usado para se referir a uma mulher ou menina.\n"
                       "5. It (Ele ou Ela) - Usado para se referir a objetos, animais ou coisas.\n"
                       "6. We (Nós) - Usado para se referir a um grupo que inclui o falante.\n"
                       "7. You (Vocês) - Usado para se referir a um grupo de pessoas.\n"
                       "8. They (Eles ou Elas) - Usado para se referir a pessoas ou coisas que não incluem o falante."),
            ("Aula 8", "Nesta aula, vamos aprender alguns adjetivos comuns em inglês.\n"
                       "1. Good (Bom) - Usado para descrever algo que é de qualidade positiva.\n"
                       "2. Bad (Ruim) - Usado para descrever algo que é de qualidade negativa.\n"
                       "3. Big (Grande) - Usado para descrever algo de tamanho grande.\n"
                       "4. Small (Pequeno) - Usado para descrever algo de tamanho pequeno.\n"
                       "5. Happy (Feliz) - Usado para descrever um estado de felicidade.\n"
                       "6. Sad (Triste) - Usado para descrever um estado de tristeza.\n"
                       "7. Beautiful (Bonito) - Usado para descrever algo que é bonito ou atraente.\n"
                       "8. Ugly (Feio) - Usado para descrever algo que não é bonito ou atraente.\n"
                       "9. Hot (Quente) - Usado para descrever algo com alta temperatura.\n"
                       "10. Cold (Frio) - Usado para descrever algo com baixa temperatura."),
            ("Aula 9", "Nesta aula, vamos aprender alguns substantivos comuns em inglês.\n"
                       "1. House (Casa) - Um lugar onde as pessoas moram.\n"
                       "2. Car (Carro) - Um veículo usado para transporte.\n"
                       "3. Dog (Cachorro) - Um animal de estimação comum.\n"
                       "4. Cat (Gato) - Outro animal de estimação popular.\n"
                       "5. Book (Livro) - Um objeto usado para leitura.\n"
                       "6. Table (Mesa) - Um móvel usado para colocar coisas.\n"
                       "7. Chair (Cadeira) - Um assento comum para uma pessoa.\n"
                       "8. Computer (Computador) - Uma máquina usada para processamento de dados.\n"
                       "9. Phone (Telefone) - Um dispositivo para comunicação.\n"
                       "10. Friend (Amigo) - Uma pessoa com quem você tem uma relação próxima."),
            ("Aula 10", "Nesta aula, vamos aprender algumas preposições comuns em inglês.\n"
                        "1. In (Em) - Usado para indicar posição dentro de algo.\n"
                        "2. On (Em/cima de) - Usado para indicar posição em cima de algo.\n"
                        "3. At (Em/a) - Usado para indicar posição específica ou localização.\n"
                        "4. By (Por/junto de) - Usado para indicar proximidade ou meio de transporte.\n"
                        "5. For (Para/por) - Usado para indicar finalidade ou benefício.\n"
                        "6. With (Com) - Usado para indicar companhia ou instrumento.\n"
                        "7. From (De) - Usado para indicar origem ou ponto de partida.\n"
                        "8. To (Para) - Usado para indicar destino ou movimento em direção a algo.\n"
                        "9. Into (Dentro em) - Usado para indicar movimento em direção ao interior de algo.\n"
                        "10. Out of (Fora de) - Usado para indicar movimento para fora de algo."),
        ]

        for lesson in self.links:
            lesson_button = tk.Button(self.progress_window, text=lesson[0], command=lambda l=lesson: self.open_lesson(l))
            lesson_button.pack(pady=5)

    def open_lesson(self, lesson):
        """Abre a lição selecionada e atualiza o progresso."""
        lesson_window = tk.Toplevel(self.root)
        lesson_window.title(lesson[0])

        lesson_label = tk.Label(lesson_window, text=lesson[1], justify=tk.LEFT, padx=10, pady=10, wraplength=380)
        lesson_label.pack()

        self.update_progress()

    def update_progress(self):
        """Atualiza a barra de progresso."""
        self.progress += 10
        self.progress_var.set(self.progress)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
