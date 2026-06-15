# vllm-project/vllm#13888: [Bug]: collect_env doesn't work in uv environment

| 字段 | 值 |
| --- | --- |
| Issue | [#13888](https://github.com/vllm-project/vllm/issues/13888) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: collect_env doesn't work in uv environment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the collect_env scripts, it fails instead of producing relevant information ``` Traceback (most recent call last): File "/home/bmuskalla/repos/X/collect_env.py", line 771, in main() File "/home/bmuskalla/repos/X/collect_env.py", line 750, in main output = get_pretty_env_info() File "/home/bmuskalla/repos/X/collect_env.py", line 745, in get_pretty_env_info return pretty_str(get_env_info()) File "/home/bmuskalla/repos/X/collect_env.py", line 543, in get_env_info pip_version, pip_list_output = get_pip_packages(run_lambda) File "/home/bmuskalla/repos/X/collect_env.py", line 497, in get_pip_packages out = run_with_pip([sys.executable, '-mpip']) File "/home/bmuskalla/repos/X/collect_env.py", line 492, in run_with_pip return "\n".join(line for line in out.splitlines() AttributeError: 'NoneType' object has no attribute 'splitlines' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the bug When running the collect_env scripts, it fails instead of producing relevant information ``` Traceback (most recent call last): File "/home/bmuskalla/repos/X/collect_env.py", line 771, in main() File "/home/bmus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: unning the collect_env scripts, it fails instead of producing relevant information ``` Traceback (most recent call last): File "/home/bmuskalla/repos/X/collect_env.py", line 771, in main() File "/home/bmuskalla/repos/X/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
