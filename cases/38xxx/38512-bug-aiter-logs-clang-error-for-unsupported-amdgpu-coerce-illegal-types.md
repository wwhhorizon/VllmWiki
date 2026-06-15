# vllm-project/vllm#38512: [Bug]: AITER logs clang error for unsupported `-amdgpu-coerce-illegal-types=1` flag during kernel compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#38512](https://github.com/vllm-project/vllm/issues/38512) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AITER logs clang error for unsupported `-amdgpu-coerce-illegal-types=1` flag during kernel compilation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vLLM speech-to-text tests with `mistralai/Voxtral-Mini-3B-2507`, the aiter library logs a clang compilation error during paged attention kernel JIT compilation. The test still passes, but the error indicates a kernel build path is hitting an unsupported compiler flag. ## Reproduction ```bash cd /app/vllm/tests pytest -s -v entrypoints/openai/speech_to_text/test_transcription_validation.py::test_basic_audio[mistralai/Voxtral-Mini-3B-2507] ``` ## Error logs ``` (EngineCore pid=126888) [aiter] start build /root/.aiter/build/pa_v1_6f4b310357f7bbad8deb56da4f1bc982 clang (LLVM option parsing): Unknown command line argument '-amdgpu-coerce-illegal-types=1'. Try: 'clang (LLVM option parsing) --help' clang (LLVM option parsing): Did you mean '--amdgpu-mode-register=1'? failed to execute:/opt/rocm/lib/llvm/bin/clang++ --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 -O3 -mllvm -amdgpu-coerce-illegal-types=1 -x hip -c /dev/null -o "/dev/null" (EngineCore pid=126888) [aiter] -mllvm -amdgpu-coerce-illegal...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: JIT compilation. The test still passes, but the error indicates a kernel build path is hitting an unsupported compiler flag. ## Reproduction ```bash cd /app/vllm/tests pytest -s -v entrypoints/openai/speech_to_text/test...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rted `-amdgpu-coerce-illegal-types=1` flag during kernel compilation bug;rocm ### Your current environment ### 🐛 Describe the bug When running vLLM speech-to-text tests with `mistralai/Voxtral-Mini-3B-2507`, the aiter l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: AITER logs clang error for unsupported `-amdgpu-coerce-illegal-types=1` flag during kernel compilation bug;rocm ### Your current environment ### 🐛 Describe the bug When running vLLM speech-to-text tests with `mis...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency Yo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: pu-mode-register=1'? failed to execute:/opt/rocm/lib/llvm/bin/clang++ --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gfx950 --offload-arch=gf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
