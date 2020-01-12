from random import choice, randint
import tkinter as tk


# Window size constants
WIDTH = 1200
HEIGHT = 800


class Generator:
    _empty_words = [
        'ну', 'как бы', 'для того чтобы',
        'в принципе', 'это самое', 'то что',
        'типа', 'тупа', 'из этого самого выходит то, что',
        'ну как бы', 'ты мне давай это самое', 'получается',
        'как его', 'короче', 'прикол',
        'походу', 'в натуре', 'собственно говоря',
        'на самом деле', 'как говорится', 'буквально'
    ]

    def __new__(cls):
        """Singleton - class must have 1 object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @classmethod
    def get_empty_word(cls):
        """Get random word from _empty_list"""
        return choice(cls._empty_words)

    def generate(self):
        """Generate the stupid text.
        
        Take a list of words, generate many TE (то есть) sentences.
        Insert the words from _empty_list into the output text
        And write the text in output_text_label
        
        """
        sentence = user_text.get()
        many_sentences = (sentence + ' ') * randint(2, 3)
        word_list = many_sentences.split(' ')
        random_index = randint(0, len(word_list))

        for i in range(randint(2, len(word_list))):
            word_list.insert(random_index, self.get_empty_word())

        for a in word_list:
            if word_list.index(a) - 1 == len(sentence.split(' ')):
                word_list.insert(word_list.index(a) - 1, 'то есть')

        output_text = ' '.join(word_list)
        output_text_label.delete(1.0, tk.END)
        output_text_label.insert(1.0, output_text)
        output_text_label.pack(pady=50)


def all_window_elements():
    """Generator obj and all labels, texts, entries, buttons"""
    global user_text, output_text_label
    
    generator = Generator()
    user_text = tk.Entry(root, width=40, font='Roboto 16', bg='#2e2d2d', fg='#fff', bd=0)
    user_text.pack(pady=30)
    
    generate_btn = tk.Button(
        text='Сгенерировать', command=generator.generate,
        bg='#2e2d2d', width=17, height=2, fg='#fff', font='Arial 20', bd=0
    )
    generate_btn.pack(pady=30)
    output_text_label = tk.Text(root, height=5, font='Roboto 14', bg='#2e2d2d', fg='#fff', bd=0)


def main():
    """Settings"""
    global root
    root = tk.Tk()
    root.title('Generator TE')
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    root.configure(background='#212121')
    
    all_window_elements()
    root.mainloop()


if __name__ == '__main__':
    main()
