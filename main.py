import cmd, sys, socket, pickle
from trame import Trame

#Instance principale de l'application de test
class Main(cmd.Cmd):
    intro = 'Xeyrus Test V0.1\n'
    prompt = '>> '

    #Démarrage de la connexion au serveur
    def do_start(self, args):
        #Définition de la socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Connexion
        s.connect(("", 1111))
        print("Connecté au serveur")

        #Envoi des messages au serveur
        message = ""
        #Boucle pour garder le prompt
        while message != "exit":
            #Saisie du message
            message = input(">> ")
            #Serialization
            trame = Trame(1, 2, message)
            trame = pickle.dumps(trame)
            #Envoi de la trame
            s.send(trame)
        #Si on saisi exit, on sort de la boucle et on se déconnecte donc du serveur
        s.close()
        print("Déconnecté du serveur")

    def do_exit(self, args):
        sys.exit(0)

if __name__ == '__main__':
    #Instanciation du prompt principal
    Main().cmdloop()
