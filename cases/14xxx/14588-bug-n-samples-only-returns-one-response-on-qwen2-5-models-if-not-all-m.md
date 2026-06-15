# vllm-project/vllm#14588: [Bug]: n samples only returns one response on Qwen2.5 models (if not all models) on V1 engine + OpenAI endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#14588](https://github.com/vllm-project/vllm/issues/14588) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: n samples only returns one response on Qwen2.5 models (if not all models) on V1 engine + OpenAI endpoint

### Issue 正文摘录

### Your current environment Dockerized vllm openai image without alternations, latest tag. I somehow cannot run the collect env script... ``` raceback (most recent call last): File "/root/collect_env.py", line 767, in main() File "/root/collect_env.py", line 746, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/root/collect_env.py", line 741, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/root/collect_env.py", line 539, in get_env_info pip_version, pip_list_output = get_pip_packages(run_lambda) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/collect_env.py", line 493, in get_pip_packages out = run_with_pip([sys.executable, '-mpip']) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/collect_env.py", line 489, in run_with_pip return "\n".join(line for line in out.splitlines() ^^^^^^^^^^^^^^ AttributeError: 'NoneType' object has no attribute 'splitlines' ``` ### 🐛 Describe the bug When turning on the V1 engine, I observed that supplying n>=1 will only receive one repsonse, when using the V0 engine, it returns N repsosnes with a index properly. This is reproduced on the latest vllm image. ``` response = client.chat.completions.create( mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: models) on V1 engine + OpenAI endpoint bug ### Your current environment Dockerized vllm openai image without alternations, latest tag. I somehow cannot run the collect env script... ``` raceback (most recent call last):...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: n samples only returns one response on Qwen2.5 models (if not all models) on V1 engine + OpenAI endpoint bug ### Your current environment Dockerized vllm openai image without alternations, latest tag. I somehow c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ing the V0 engine, it returns N repsosnes with a index properly. This is reproduced on the latest vllm image. ``` response = client.chat.completions.create( model='vllm-qwen-coder-7b-instruct', #model='gpt-4o', messages...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: urrent environment Dockerized vllm openai image without alternations, latest tag. I somehow cannot run the collect env script... ``` raceback (most recent call last): File "/root/collect_env.py", line 767, in main() Fil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
