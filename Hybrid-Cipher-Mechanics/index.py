import HybridEncoDeco.sPlayfairCipher as sPlayfairCipher
import HybridEncoDeco.sPolyalphabatic as sPolyalphabatic
import HybridEncoDeco.tRailFenceTransposition as tRailFenceTransposition
import HybridEncoDeco.sCeaserCipher as sCeaserCipher

c2 = sPlayfairCipher.playfair_encrypt("Rohit Nittawadekar", "Rohit")
d2 = sPlayfairCipher.playfair_decrypt(c2, "Rohit")

print(c2)
print(d2)

kk = 30
c1 = tRailFenceTransposition.rail_fence_encrypt("Rohit Nittawadekar", kk)
d1 = tRailFenceTransposition.rail_fence_decrypt(c1, kk)

print(c1)
print(d1)

c = sPolyalphabatic.polyalphabetic_encrypt("Rohit Nittawadekar", "raman")
d = sPolyalphabatic.polyalphabetic_decrypt(c, "raman")

print(c)
print(d)


c3 = sCeaserCipher.ceaser_encrypt("Rohit Nittawadekar", 3)
d3 = sCeaserCipher.ceaser_decrypt(c3, 3)

print(c3)
print(d3)
print("Hybrid Cipher Mechanics")