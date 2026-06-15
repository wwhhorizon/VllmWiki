# vllm-project/vllm#14734: [Usage]: Tool calling for gemma-3

| 字段 | 值 |
| --- | --- |
| Issue | [#14734](https://github.com/vllm-project/vllm/issues/14734) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 36; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Tool calling for gemma-3

### Issue 正文摘录

### Your current environment Collecting environment information... Traceback (most recent call last): File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 767, in main() File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 746, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 741, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 570, in get_env_info vllm_version = get_vllm_version() ^^^^^^^^^^^^^^^^^^ File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 275, in get_vllm_version from vllm import __version__, __version_tuple__ ImportError: cannot import name '__version__' from 'vllm' (unknown location) ### How would you like to use vllm I've seen reports that Gemma-3 supports function calling (also known as tool calling). I'm particularly interested in using this feature with vLLM, but I haven't been able to find any documentation or examples on how to implement it for gemma-3. Could you please provide information on: Whether vLLM currently supports Gemma-3's tool calling/function...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: urakhim/gemma_3_test/collect_env.py", line 570, in get_env_info vllm_version = get_vllm_version() ^^^^^^^^^^^^^^^^^^ File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 275, in get_vllm_version from vllm i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Tool calling for gemma-3 usage ### Your current environment Collecting environment information... Traceback (most recent call last): File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 767, in mai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: Tool calling for gemma-3 usage ### Your current environment Collecting environment information... Traceback (most recent call last): File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 767, in mai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ceback (most recent call last): File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 767, in main() File "/opt/ai_users/abdurakhim/gemma_3_test/collect_env.py", line 746, in main output = get_pretty_env_inf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
