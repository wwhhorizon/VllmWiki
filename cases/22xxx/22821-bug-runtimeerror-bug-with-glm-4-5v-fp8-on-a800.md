# vllm-project/vllm#22821: [Bug]: RuntimeError bug with GLM-4.5V-FP8 on A800

| 字段 | 值 |
| --- | --- |
| Issue | [#22821](https://github.com/vllm-project/vllm/issues/22821) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError bug with GLM-4.5V-FP8 on A800

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying [GLM-4.5V-FP8](https://huggingface.co/zai-org/GLM-4.5V-FP8) model on A800, encounter the following error: ```text (EngineCore_0 pid=1480388) (VllmWorker TP0 pid=1480410) INFO 08-13 14:46:28 [default_loader.py:262] Loading weights took 26.38 seconds WARNING 08-13 14:46:28 [marlin_utils_fp8.py:82] Your GPU does not have native support for FP8 computation but FP8 quantization is being used. Weight-only FP8 compression will be used leveraging the Marlin kernel. This may degrade performance for compute-heavy workloads. INFO 08-13 14:46:29 [gpu_model_runner.py:1996] Model loading took 51.2606 GiB and 28.918477 seconds INFO 08-13 14:46:31 [gpu_model_runner.py:1996] Model loading took 51.2606 GiB and 29.061120 seconds INFO 08-13 14:46:31 [gpu_model_runner.py:2499] Encoder cache will be initialized with a budget of 30970 tokens, and profiled with 1 video items of the maximum feature size. INFO 08-13 14:46:31 [gpu_model_runner.py:2499] Encoder cache will be initialized with a budget of 30970 tokens, and profiled with 1 video items of the maximum feature size. ERROR 08-13 14:51:19 [multiproc_executor.py:596] WorkerProc hit an ex...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: vironment ### 🐛 Describe the bug When trying [GLM-4.5V-FP8](https://huggingface.co/zai-org/GLM-4.5V-FP8) model on A800, encounter the following error: ```text (EngineCore_0 pid=1480388) (VllmWorker TP0 pid=1480410) INFO...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: core.py:684] EngineCore failed to start. ``` ## Reproduce Code ```python import vllm from vllm import SamplingParams from vllm.lora.request import LoRARequest from vllm.config import CompilationConfig MODEL= "zai-org/GL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: RuntimeError bug with GLM-4.5V-FP8 on A800 bug ### Your current environment ### 🐛 Describe the bug When trying [GLM-4.5V-FP8](https://huggingface.co/zai-org/GLM-4.5V-FP8) model on A800, encounter the following er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: py:596] File "/root/Code/vllm_dev/vllm/vllm/model_executor/models/glm4_moe.py", line 445, in forward ERROR 08-13 14:51:19 [multiproc_executor.py:596] hidden_states, residual = layer(positions, hidden_states, residual) E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
