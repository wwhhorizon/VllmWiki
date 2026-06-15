# vllm-project/vllm#8065: [Usage]: Using TPU example with InternVL2 Model

| 字段 | 值 |
| --- | --- |
| Issue | [#8065](https://github.com/vllm-project/vllm/issues/8065) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Using TPU example with InternVL2 Model

### Issue 正文摘录

### Your current environment ``` Collecting environment information... Traceback (most recent call last): File "/home/kojoe/EasyAnimate/easyanimate/image_caption/collect_env.py", line 735, in main() File "/home/kojoe/EasyAnimate/easyanimate/image_caption/collect_env.py", line 714, in main output = get_pretty_env_info() File "/home/kojoe/EasyAnimate/easyanimate/image_caption/collect_env.py", line 709, in get_pretty_env_info return pretty_str(get_env_info()) File "/home/kojoe/EasyAnimate/easyanimate/image_caption/collect_env.py", line 510, in get_env_info pip_version, pip_list_output = get_pip_packages(run_lambda) File "/home/kojoe/EasyAnimate/easyanimate/image_caption/collect_env.py", line 480, in get_pip_packages out = run_with_pip([sys.executable, '-mpip']) File "/home/kojoe/EasyAnimate/easyanimate/image_caption/collect_env.py", line 476, in run_with_pip return "\n".join(line for line in out.splitlines() AttributeError: 'NoneType' object has no attribute 'splitlines' ``` ### How would you like to use vllm I want to run inference of a [OpenGVLab/InternVL2-8B](https://huggingface.co/OpenGVLab/InternVL2-8B). I don't know how to integrate it with vllm. ### Before submitting a new iss...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Using TPU example with InternVL2 Model usage;stale ### Your current environment ``` Collecting environment information... Traceback (most recent call last): File "/home/kojoe/EasyAnimate/easyanimate/image_capti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: animate/image_caption/collect_env.py", line 510, in get_env_info pip_version, pip_list_output = get_pip_packages(run_lambda) File "/home/kojoe/EasyAnimate/easyanimate/image_caption/collect_env.py", line 480, in get_pip_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Using TPU example with InternVL2 Model usage;stale ### Your current environment ``` Collecting environment information... Traceback (most recent call last): File "/home/kojoe/EasyAnimate/easyanimate/image_capti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
