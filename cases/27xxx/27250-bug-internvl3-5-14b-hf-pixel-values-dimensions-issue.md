# vllm-project/vllm#27250: [Bug]: Internvl3_5-14B-HF pixel_values dimensions issue

| 字段 | 值 |
| --- | --- |
| Issue | [#27250](https://github.com/vllm-project/vllm/issues/27250) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Internvl3_5-14B-HF pixel_values dimensions issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Facing issues with pixel dimensions when running the cli vllm serve command. All running on a single 80GB H100 GPU. The dimensions of the image seem to be misaligned, however I am not running inference and only on start up through the vllm serve command. I am not entirely sure where this error comes from and this might be unrelated but checking the internvl3_5 usage examples on hugginface (https://huggingface.co/OpenGVLab/InternVL3_5-14B ) it does use the default dimension size is 448 where as it seems the example media by vllm is 384. The cli vllm serve command i used ```text CUDA_VISIBLE_DEVICES=0 vllm serve OpenGVLab/InternVL3_5-14B-HF --port 8125 --gpu-memory-utilization 0.70 --max-model-len 28k --trust-remote-code --limit-mm-per-prompt '{"image":1}' ``` The output and the traceback error: ```text (EngineCore_DP0 pid=2124694) INFO 10-21 06:46:15 [gpu_model_runner.py:2653] Model loading took 28.1727 GiB and 7.349091 seconds (EngineCore_DP0 pid=2124694) INFO 10-21 06:46:16 [gpu_model_runner.py:3344] Encoder cache will be initialized with a budget of 28511 tokens, and profiled with 1 video items of the maximum feature size. (Eng...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Internvl3_5-14B-HF pixel_values dimensions issue bug ### Your current environment ### 🐛 Describe the bug Facing issues with pixel dimensions when running the cli vllm serve command. All running on a single 80GB H...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ons issue bug ### Your current environment ### 🐛 Describe the bug Facing issues with pixel dimensions when running the cli vllm serve command. All running on a single 80GB H100 GPU. The dimensions of the image seem to b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ns when running the cli vllm serve command. All running on a single 80GB H100 GPU. The dimensions of the image seem to be misaligned, however I am not running inference and only on start up through the vllm serve comman...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 44] Encoder cache will be initialized with a budget of 28511 tokens, and profiled with 1 video items of the maximum feature size. (EngineCore_DP0 pid=2124694) ERROR 10-21 06:46:16 [core.py:708] EngineCore failed to star...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
