# vllm-project/vllm#14534: [Bug]: [V1] Molmo/Aria not supported on V1 due to xgrammar

| 字段 | 值 |
| --- | --- |
| Issue | [#14534](https://github.com/vllm-project/vllm/issues/14534) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1] Molmo/Aria not supported on V1 due to xgrammar

### Issue 正文摘录

### Your current environment Cannot use these models on V1 due to Xgrammar assert ### 🐛 Describe the bug - run the following ```bash VLLM_USE_V1=1 pytest -s -x models/decoder_only/vision_language/test_models.py -k molmo VLLM_USE_V1=1 pytest -s -x models/decoder_only/vision_language/test_models.py -k aria ``` - get the following back ```bash ERROR 03-10 03:06:35 [core.py:324] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-10 03:06:35 [core.py:324] File "/home/rshaw/vllm/vllm/v1/engine/core.py", line 316, in run_engine_core ERROR 03-10 03:06:35 [core.py:324] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-10 03:06:35 [core.py:324] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-10 03:06:35 [core.py:324] File "/home/rshaw/vllm/vllm/v1/engine/core.py", line 271, in __init__ ERROR 03-10 03:06:35 [core.py:324] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-10 03:06:35 [core.py:324] File "/home/rshaw/vllm/vllm/v1/engine/core.py", line 65, in __init__ ERROR 03-10 03:06:35 [core.py:324] self.structured_output_manager = StructuredOutputManager(vllm_config) ERROR 03-10 03:06:35 [core.py:324] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-10 03:06:3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mar bug;structured-output ### Your current environment Cannot use these models on V1 due to Xgrammar assert ### 🐛 Describe the bug - run the following ```bash VLLM_USE_V1=1 pytest -s -x models/decoder_only/vision_langua...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cab ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e the bug - run the following ```bash VLLM_USE_V1=1 pytest -s -x models/decoder_only/vision_language/test_models.py -k molmo VLLM_USE_V1=1 pytest -s -x models/decoder_only/vision_language/test_models.py -k aria ``` - ge...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ert ### 🐛 Describe the bug - run the following ```bash VLLM_USE_V1=1 pytest -s -x models/decoder_only/vision_language/test_models.py -k molmo VLLM_USE_V1=1 pytest -s -x models/decoder_only/vision_language/test_models.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
