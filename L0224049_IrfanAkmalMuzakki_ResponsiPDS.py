import numpy as np
import matplotlib.pyplot as plt

N_ITERATIONS = 50000  

x = np.random.uniform(0, 1, N_ITERATIONS)
y = np.random.uniform(0, 1, N_ITERATIONS)


distance_sq = x**2 + y**2

points_inside = distance_sq <= 1

C = np.sum(points_inside) 
pi_estimate = 4 * (C / N_ITERATIONS)

print("===========================================")
print("           HASIL SIMULASI PI               ")
print("===========================================")
print(f"Total Titik (N)          : {N_ITERATIONS:,}")
print(f"Titik di Dalam Lingkaran (C): {C:,}")
print(f"Estimasi Nilai Pi        : {pi_estimate:.6f}")
print(f"Nilai Pi Sebenarnya      : {np.pi:.6f}")
print(f"Error Absolut            : {abs(pi_estimate - np.pi):.6e}")
print("===========================================")


plt.figure(figsize=(8, 8))

x_in = x[points_inside]
y_in = y[points_inside]
x_out = x[~points_inside]
y_out = y[~points_inside]


plt.scatter(x_out, y_out, color='red', s=1, alpha=0.6, label='Luar Lingkaran')
plt.scatter(x_in, y_in, color='green', s=1, alpha=0.8, label='Dalam Lingkaran')


plt.plot([0, 1], [0, 0], color='black', linewidth=2)
plt.plot([0, 0], [0, 1], color='black', linewidth=2)


t = np.linspace(0, np.pi/2, 100)
plt.plot(np.cos(t), np.sin(t), color='blue', linestyle='--', linewidth=2, label='Batas Lingkaran')


plt.title(f'Simulasi Monte Carlo Estimasi $\pi$ (N={N_ITERATIONS:,})', fontsize=14)
plt.xlabel('Koordinat X')
plt.ylabel('Koordinat Y')
plt.legend(markerscale=10)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True, linestyle=':', alpha=0.5)
plt.show()

cumulative_pi = 4 * (np.cumsum(points_inside) / np.arange(1, N_ITERATIONS + 1))

plt.figure(figsize=(10, 5))
plt.plot(np.arange(1, N_ITERATIONS + 1), cumulative_pi, label='Estimasi $\pi$', color='orange')
plt.axhline(np.pi, color='blue', linestyle='--', label='Nilai $\pi$ Sebenarnya')

plt.title('Konvergensi Estimasi $\pi$ Terhadap Jumlah Iterasi', fontsize=14)
plt.xlabel('Jumlah Iterasi (N)', fontsize=12)
plt.ylabel('Nilai Estimasi $\pi$', fontsize=12)
plt.xscale('log')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()