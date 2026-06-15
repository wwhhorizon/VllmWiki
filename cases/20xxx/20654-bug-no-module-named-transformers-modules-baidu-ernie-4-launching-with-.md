# vllm-project/vllm#20654: [Bug]: No module named 'transformers_modules.baidu.ERNIE-4 launching with vLLM 0.9.2rc2.dev #

| 字段 | 值 |
| --- | --- |
| Issue | [#20654](https://github.com/vllm-project/vllm/issues/20654) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: No module named 'transformers_modules.baidu.ERNIE-4 launching with vLLM 0.9.2rc2.dev #

### Issue 正文摘录

### Your current environment It's not finding the config files in the repo directory? 0.9.2rc2.dev78+g71d1d75b7.d20250708.cu129 I tried: vllm serve baidu/ERNIE-4.5-VL-28B-A3B-PT --trust-remote-code -tp 2 downloaded locally: vllm serve /mnt/models/baidu/ERNIE-4.5-VL-28B-A3B-PT --trust-remote-code -tp 2 ### 🐛 Describe the bug errors: File "/home/strong/.cache/huggingface/modules/transformers_modules/baidu/ERNIE-4.5-VL-28B-A3B-PT/39a152ff17303939b06edc1b8d1a2ea7b31e8ec7/processing_ernie_45t_vl.py", line 46, in (VllmWorker rank=0 pid=95272) ERROR 07-09 03:23:09 [multiproc_executor.py:487] from .tokenization_ernie_45t_vl import Ernie4_5_VLTokenizer (VllmWorker rank=0 pid=95272) ERROR 07-09 03:24:09 [multiproc_executor.py:487] ModuleNotFoundError: No module named 'transformers_modules.baidu.ERNIE-4' File "/home/strong/.cache/huggingface/modules/transformers_modules/ERNIE-4.5-VL-28B-A3B-PT/processing_ernie_45t_vl.py", line 46, in ERROR 07-09 03:24:16 [core.py:586] from .tokenization_ernie_45t_vl import Ernie4_5_VLTokenizer ERROR 07-09 03:24:16 [core.py:586] ModuleNotFoundError: No module named 'transformers_modules.ERNIE-4.5-VL-28B-A3B-PT' Process ### Before submitting a new issue... - [...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: .2rc2.dev # bug;stale ### Your current environment It's not finding the config files in the repo directory? 0.9.2rc2.dev78+g71d1d75b7.d20250708.cu129 I tried: vllm serve baidu/ERNIE-4.5-VL-28B-A3B-PT --trust-remote-code...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -09 03:23:09 [multiproc_executor.py:487] from .tokenization_ernie_45t_vl import Ernie4_5_VLTokenizer (VllmWorker rank=0 pid=95272) ERROR 07-09 03:24:09 [multiproc_executor.py:487] ModuleNotFoundError: No module named 't...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ess ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ransformers_modules.baidu.ERNIE-4 launching with vLLM 0.9.2rc2.dev # bug;stale ### Your current environment It's not finding the config files in the repo directory? 0.9.2rc2.dev78+g71d1d75b7.d20250708.cu129 I tried: vll...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
