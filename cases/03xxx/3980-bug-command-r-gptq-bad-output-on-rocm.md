# vllm-project/vllm#3980: [Bug]: Command R+ GPTQ bad output on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#3980](https://github.com/vllm-project/vllm/issues/3980) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Command R+ GPTQ bad output on ROCm

### Issue 正文摘录

### Your current environment [env.txt](https://github.com/vllm-project/vllm/files/14937936/env.txt) ### 🐛 Describe the bug When loading this [model](https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ) using a docker image built from source as of 2024-04-09, every prompt outputs a single token on repeat. ![image](https://github.com/vllm-project/vllm/assets/7338884/d1945c0b-414d-4a7a-a26b-98d8f1e8a096) This also happens when using the OpenAI API, usually outputting nothing but punctuation. I have tried changing the max_position_embeddings to equal model_max_length to no avail as discussed here https://github.com/vllm-project/vllm/issues/3892, along with building again after the PR was merged (I checked that [vllm/model_executor/models/commandr.py](https://github.com/vllm-project/vllm/pull/3919/files#diff-621e091acd96c946ebc4c4b602f5045b00b5f4f8e66e65754bfcb3fb861b80ec) matches the PR, and it does) This is on a 4x AMD Instinct MI100 system with a GPU bridge, applying the fixes in Dockerfile.rocm to update the FA branch, FA arch, and the numpy fix prior to today's PR https://github.com/vllm-project/vllm/pull/3962

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: odel](https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ) using a docker image built from source as of 2024-04-09, every prompt outputs a single token on repeat. ![image](https://github.com/vllm-project/vllm/asse...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Command R+ GPTQ bad output on ROCm bug ### Your current environment [env.txt](https://github.com/vllm-project/vllm/files/14937936/env.txt) ### 🐛 Describe the bug When loading this [model](https://huggingface.co/a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vllm/files/14937936/env.txt) ### 🐛 Describe the bug When loading this [model](https://huggingface.co/alpindale/c4ai-command-r-plus-GPTQ) using a docker image built from source as of 2024-04-09, every prompt outputs a si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
