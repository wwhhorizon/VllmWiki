# vllm-project/vllm#35602: [Bug]:  vllm: error: unrecognized arguments: --language-model-only

| 字段 | 值 |
| --- | --- |
| Issue | [#35602](https://github.com/vllm-project/vllm/issues/35602) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  vllm: error: unrecognized arguments: --language-model-only

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` caoyizhen in 🌐 zkrj-SYS-740GP-TNRT in caoyizhen/research/vllm_yaml via 🐍 v3.12.11 (vllm_env) ❯ CUDA_VISIBLE_DEVICES=1 vllm serve /data2/open-source-model/Qwen3.5-27B --port 6270 --tensor-parallel-size 1 --max-model-len 8000 --reasoning-parser qwen3 --language-model-only usage: vllm [-h] [-v] {chat,complete,serve,bench,collect-env,run-batch} ... vllm: error: unrecognized arguments: --language-model-only caoyizhen in 🌐 zkrj-SYS-740GP-TNRT in caoyizhen/research/vllm_yaml via 🐍 v3.12.11 (vllm_env) took 11s ❯ uv pip list |grep vllm vllm 0.16.0 caoyizhen in 🌐 zkrj-SYS-740GP-TNRT in caoyizhen/research/vllm_yaml via 🐍 v3.12.11 (vllm_env) ❯ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Describe the bug ``` caoyizhen in 🌐 zkrj-SYS-740GP-TNRT in caoyizhen/research/vllm_yaml via 🐍 v3.12.11 (vllm_env) ❯ CUDA_VISIBLE_DEVICES=1 vllm serve /data2/open-source-model/Qwen3.5-27B --port 6270 --tensor-parallel-si...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm: error: unrecognized arguments: --language-model-only bug ### Your current environment ### 🐛 Describe the bug ``` caoyizhen in 🌐 zkrj-SYS-740GP-TNRT in caoyizhen/research/vllm_yaml via 🐍 v3.12.11 (vllm_env)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
