# vllm-project/vllm#41964: [Bug]:  VLLM:EngineCore thread consumes 100% CPU idle on ROCm/Radeon AI Pro 9700

| 字段 | 值 |
| --- | --- |
| Issue | [#41964](https://github.com/vllm-project/vllm/issues/41964) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  VLLM:EngineCore thread consumes 100% CPU idle on ROCm/Radeon AI Pro 9700

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m serving a FP8-quant of gemma-4 E4B on a Radeon AI Pro 9700 with vLLM and things perform and scale wonderfully. However, even when no requests are processed, one CPU core is at 100% busy all the time (kept busy by a VLLM:EngineCore thread, according to htop). The setup of my test environment: - Ryzen 1600AF (basically a 2600), 6 cores/12 threads with 16 GB of RAM - Linux Mint 22.3 (Ubuntu 24.04 based) - one Radeon AI Pro 9700 - ROCm 7.2.2 Installed vLLM 0.20.1 in a Python venv: ``` pip install vllm==0.20.1+rocm721 --extra-index-url https://wheels.vllm.ai/rocm/0.20.1/rocm721 ``` The vllm command line: ``` vllm serve \ --served-model-name=local-gemma4 \ --max-model-len 128k \ --enable-auto-tool-choice \ --reasoning-parser gemma4 \ --tool-call-parser gemma4 \ ``` There are old reports that on the surface read related (issue #16968), however, this should have been solved first by PR #16226 which introduced VLLM_SLEEP_WHEN_IDLE=1, and then by another overhaul via PR #28053 which superseded that earlier patch as far as I can tell. I wonder if this is a Radeon AI Pro 9700 specific issue, there seem to be other problems regarding vLLM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ux Mint 22.3 (Ubuntu 24.04 based) - one Radeon AI Pro 9700 - ROCm 7.2.2 Installed vLLM 0.20.1 in a Python venv: ``` pip install vllm==0.20.1+rocm721 --extra-index-url https://wheels.vllm.ai/rocm/0.20.1/rocm721 ``` The v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: m ### Your current environment ### 🐛 Describe the bug I’m serving a FP8-quant of gemma-4 E4B on a Radeon AI Pro 9700 with vLLM and things perform and scale wonderfully. However, even when no requests are processed, one...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: VLLM:EngineCore thread consumes 100% CPU idle on ROCm/Radeon AI Pro 9700 bug;rocm ### Your current environment ### 🐛 Describe the bug I’m serving a FP8-quant of gemma-4 E4B on a Radeon AI Pro 9700 with vLLM and t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rrent environment ### 🐛 Describe the bug I’m serving a FP8-quant of gemma-4 E4B on a Radeon AI Pro 9700 with vLLM and things perform and scale wonderfully. However, even when no requests are processed, one CPU core is a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: th vLLM and things perform and scale wonderfully. However, even when no requests are processed, one CPU core is at 100% busy all the time (kept busy by a VLLM:EngineCore thread, according to htop). The setup of my test...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
