# vllm-project/vllm#41663: [Bug]: XPU TP=2 on dual Intel Arc Pro B70 (Battlemage): GP fault + xe BCS engine reset reproduces in intel/vllm:0.17.0-xpu on Ubuntu 24.04 HWE 6.17

| 字段 | 值 |
| --- | --- |
| Issue | [#41663](https://github.com/vllm-project/vllm/issues/41663) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: XPU TP=2 on dual Intel Arc Pro B70 (Battlemage): GP fault + xe BCS engine reset reproduces in intel/vllm:0.17.0-xpu on Ubuntu 24.04 HWE 6.17

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary `intel/vllm:0.17.0-xpu` reproduces a `VLLM::Worker` general protection fault followed by `xe` BCS engine resets on a dual Intel Arc Pro B70 system when running Qwen3-30B-A3B with TP=2 and dynamic FP8 on Ubuntu 24.04.4 HWE kernel 6.17. The same failure pattern also reproduces with our local source-built vLLM XPU image. This suggests the issue is not caused by our source build alone, but likely involves an interaction between the host stack, `xe` driver/firmware, PCIe topology, and vLLM XPU TP=2 worker initialization / ProcessGroupXCCL path. A standalone XCCL/SYCL collective sweep passes on the same host, so this does not appear to be a generic oneCCL/SYCL collective failure. ## Hardware - 2× Intel Arc Pro B70 32GB, Battlemage G31, device `8086:e223` - Z890 motherboard with PCIe switch topology - No XeLink between GPUs - `p2p_access:0` - Each B70 reports PCIe 5.0 x8 host link - `ZE_AFFINITY_MASK=0,1` used for the two B70 GPUs ## Host stack - OS: Ubuntu 24.04.4 LTS - Kernel: `6.17.0-23-generic` HWE - GPU driver: in-kernel `xe` - GuC firmware: `70.44.1` - GuC firmware version 70.49.4 has been mentioned in upstream contexts...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: uilt vLLM XPU image. This suggests the issue is not caused by our source build alone, but likely involves an interaction between the host stack, `xe` driver/firmware, PCIe topology, and vLLM XPU TP=2 worker initializati...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ntel Arc Pro B70 system when running Qwen3-30B-A3B with TP=2 and dynamic FP8 on Ubuntu 24.04.4 HWE kernel 6.17. The same failure pattern also reproduces with our local source-built vLLM XPU image. This suggests the issu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: y `xe` BCS engine resets on a dual Intel Arc Pro B70 system when running Qwen3-30B-A3B with TP=2 and dynamic FP8 on Ubuntu 24.04.4 HWE kernel 6.17. The same failure pattern also reproduces with our local source-built vL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: th - Dynamic FP8 quantization via `--quantization fp8` - Tensor parallelism: `--tensor-parallel-size 2` Common args: ```bash --dtype float16 --quantization fp8 --tensor-parallel-size 2 --gpu-memory-utilization 0.88 --ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: een mentioned in upstream contexts as a newer candidate; we have not yet tested an upgrade. ## Containers tested ### Intel pre-built image - `intel/vllm:0.17.0-xpu` - Tested digest prefix: `sha256:e961d08135a6...` Intel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
