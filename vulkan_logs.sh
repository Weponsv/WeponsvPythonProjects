echo "=== Vulkan Check ===" && \
grep -i "vulkan\|lavapipe" ~/.minecraft/logs/latest.log && \
echo "=== Renderer Info ===" && \
grep -i "renderer" ~/.minecraft/logs/latest.log | head -5 && \
echo "=== Graphics Backend ===" && \
grep -i "glfw\|opengl" ~/.minecraft/logs/latest.log | head -5
