from PIL import Image

class Cube(object):

    def __init__(self, size):
        self.size = size
        self.up = Image.new("RGB",(self.size,self.size),color=(255,255,255))#white
        self.left = Image.new("RGB",(self.size,self.size),color=(255,0,0))#red
        self.front = Image.new("RGB",(self.size,self.size),color=(0,0,255))#blue
        self.right = Image.new("RGB",(self.size,self.size),color=(255,165,0))#orange
        self.back = Image.new("RGB",(self.size,self.size),color=(0,255,0))#green
        self.down = Image.new("RGB",(self.size,self.size),color=(255,255,0))#yellow

    def l(self):
        self.left = self.left.rotate(-90,expand=True)
        img_tmp = self.up.crop((0, 0, self.size / 3,self.size))
        self.up.paste(self.back.crop((0, 0, self.size / 3,self.size)), (0,0))
        self.back.paste(self.down.crop((0, 0, self.size / 3,self.size)), (0,0))
        self.down.paste(self.front.crop((0, 0, self.size / 3,self.size)), (0,0))
        self.front.paste(img_tmp, (0,0))

    def f(self):
        self.front = self.front.rotate(-90,expand=True)
        img_tmp = self.up.crop((0, self.size * 2/3, self.size,self.size)).rotate(-90,expand=True)
        self.up.paste(self.left.crop((self.size * 2/3, 0, self.size,self.size)).rotate(-90,expand=True), (0, self.size * 2/3))
        self.left.paste(self.down.crop((0, 0, self.size, self.size / 3)).rotate(-90,expand=True), (self.size * 2/3, 0))
        self.down.paste(self.right.crop((0, 0, self.size / 3,self.size)).rotate(-90,expand=True), (0,0))
        self.right.paste(img_tmp, (0,0))

    def r(self):
        self.right = self.right.rotate(-90,expand=True)
        img_tmp = self.up.crop((self.size * 2/3, 0, self.size,self.size))
        self.up.paste(self.front.crop((self.size * 2/3, 0, self.size,self.size)), (self.size * 2/3,0))
        self.front.paste(self.down.crop((self.size * 2/3, 0, self.size,self.size)), (self.size * 2/3,0))
        self.down.paste(self.back.crop((self.size * 2/3, 0, self.size,self.size)), (self.size * 2/3,0))
        self.back.paste(img_tmp, (self.size * 2/3,0))

    def b(self):
        self.back = self.back.rotate(-90,expand=True)
        img_tmp = self.up.crop((0, 0, self.size, self.size / 3)).rotate(90,expand=True)
        self.up.paste(self.right.crop((self.size * 2/3, 0, self.size,self.size)).rotate(90,expand=True), (0,0))
        self.right.paste(self.down.crop((0, self.size * 2/3, self.size, self.size)).rotate(90,expand=True), (self.size * 2/3, 0))
        self.down.paste(self.left.crop((0, 0, self.size / 3,self.size)).rotate(90,expand=True), (0,self.size * 2/3))
        self.left.paste(img_tmp, (0,0))

    def u(self):
        self.up = self.up.rotate(-90,expand=True)
        img_tmp = self.left.crop((0,0,self.size,self.size / 3)).rotate(180,expand=True)
        self.left.paste(self.front.crop((0, 0, self.size, self.size / 3)), (0, 0))
        self.front.paste(self.right.crop((0, 0, self.size, self.size / 3)), (0, 0))
        self.right.paste(self.back.crop((0, self.size * 2/3, self.size, self.size)).rotate(180,expand=True), (0, 0))
        self.back.paste(img_tmp, (0,self.size * 2/3))

    def d(self):
        self.down = self.down.rotate(-90,expand=True)
        img_tmp = self.right.crop((0,self.size * 2/3,self.size,self.size)).rotate(180,expand=True)
        self.right.paste(self.front.crop((0, self.size * 2/3, self.size, self.size)), (0, self.size * 2/3))
        self.front.paste(self.left.crop((0, self.size * 2/3, self.size, self.size)), (0, self.size * 2/3))
        self.left.paste(self.back.crop((0, 0, self.size, self.size / 3)).rotate(180,expand=True), (0, self.size * 2/3))
        self.back.paste(img_tmp, (0,0))

    @staticmethod
    def add_grid(img):
        size = img.size[0]
        vertical = Image.new("RGB", (4, size), color=(0,0,0))
        horizontal = vertical.rotate(90,expand=True)

        img_grill = img.copy()

        img_grill.paste(vertical,(size / 3 - 2,0))
        img_grill.paste(vertical,(size * 2/3 - 2,0))
        img_grill.paste(horizontal,(0,size / 3 - 2))
        img_grill.paste(horizontal,(0,size * 2/3 - 2))

        return img_grill


    def get_image(self):
        img = Image.new("RGB",(self.size*3,self.size*4), color=(0,0,0))
        img.paste(Cube.add_grid(self.up), (self.size,0))
        img.paste(Cube.add_grid(self.front), (self.size,self.size))
        img.paste(Cube.add_grid(self.left), (0,self.size))
        img.paste(Cube.add_grid(self.right), (self.size*2,self.size))
        img.paste(Cube.add_grid(self.down), (self.size,self.size*2))
        img.paste(Cube.add_grid(self.back), (self.size,self.size*3))
        return img.rotate(90,expand=True)

    def save(self):
        self.up.save("up.png")
        self.front.save("front.png")
        self.left.save("left.png")
        self.right.save("right.png")
        self.back.save("back.png")
        self.down.save("down.png")

    def execute(self, cmd):
        cmd = cmd.lower()
        cmd = list(cmd)
        cmd.append("#")
        i = 0
        while i < len(cmd)-1:
            if cmd[i] == "l":
                i += 1
                if cmd[i] == "'":
                    i += 1
                    self.l_()
                else:
                    self.l()
            elif cmd[i] == "f":
                i += 1
                if cmd[i] == "'":
                    i += 1
                    self.f_()
                else:
                    self.f()
            elif cmd[i] == "r":
                i += 1
                if cmd[i] == "'":
                    i += 1
                    self.r_()
                else:
                    self.r()
            elif cmd[i] == "b":
                i += 1
                if cmd[i] == "'":
                    i += 1
                    self.b_()
                else:
                    self.b()
            elif cmd[i] == "u":
                i += 1
                if cmd[i] == "'":
                    i += 1
                    self.u_()
                else:
                    self.u()
            elif cmd[i] == "d":
                i += 1
                if cmd[i] == "'":
                    i += 1
                    self.d_()
                else:
                    self.d()

    def l_(self):
        self.l()
        self.l()
        self.l()

    def f_(self):
        self.f()
        self.f()
        self.f()

    def r_(self):
        self.r()
        self.r()
        self.r()

    def b_(self):
        self.b()
        self.b()
        self.b()

    def u_(self):
        self.u()
        self.u()
        self.u()

    def d_(self):
        self.d()
        self.d()
        self.d()
