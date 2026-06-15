# vllm-project/vllm#24063: [Bug]: In `uv` venv, running `python collect_env.py` will return error.

| 字段 | 值 |
| --- | --- |
| Issue | [#24063](https://github.com/vllm-project/vllm/issues/24063) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In `uv` venv, running `python collect_env.py` will return error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If using uv run to execute it, since `collect_env.py` is designed to gather environment information, it should be read-only to the system and should not modify the environment. Therefore, using `uv run` is not appropriate. relate to: #15792 To reproduce: ``` (vllm-cpu) root@gpu-3090:~/oss/vllm-cpu# python vllm/collect_env.py Collecting environment information... Traceback (most recent call last): File "/root/oss/vllm-cpu/vllm/collect_env.py", line 825, in main() File "/root/oss/vllm-cpu/vllm/collect_env.py", line 804, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/root/oss/vllm-cpu/vllm/collect_env.py", line 799, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/root/oss/vllm-cpu/vllm/collect_env.py", line 574, in get_env_info pip_version, pip_list_output = get_pip_packages(run_lambda) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/oss/vllm-cpu/vllm/collect_env.py", line 529, in get_pip_packages out = run_with_pip() ^^^^^^^^^^^^^^ File "/root/oss/vllm-cpu/vllm/collect_env.py", line 520, in run_with_pip raise RuntimeError( RuntimeError: Could not collect pip list output (pip or uv module...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oot/oss/vllm-cpu/vllm/collect_env.py", line 574, in get_env_info pip_version, pip_list_output = get_pip_packages(run_lambda) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/oss/vllm-cpu/vllm/collect_env.py", line 529, in get_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: o execute it, since `collect_env.py` is designed to gather environment information, it should be read-only to the system and should not modify the environment. Therefore, using `uv run` is not appropriate. relate to: #1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ent. Therefore, using `uv run` is not appropriate. relate to: #15792 To reproduce: ``` (vllm-cpu) root@gpu-3090:~/oss/vllm-cpu# python vllm/collect_env.py Collecting environment information... Traceback (most recent cal...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
