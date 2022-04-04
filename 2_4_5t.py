
class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life) + ' life(s) left')



enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

enemy1.attack()
enemy1.checkLife()
enemy2.attack()
enemy2.checkLife()
enemy3.attack()
enemy3.checkLife()