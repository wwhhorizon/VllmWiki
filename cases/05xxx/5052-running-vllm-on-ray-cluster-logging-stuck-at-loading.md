# vllm-project/vllm#5052: Running Vllm on ray cluster, logging stuck at loading

| 字段 | 值 |
| --- | --- |
| Issue | [#5052](https://github.com/vllm-project/vllm/issues/5052) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Running Vllm on ray cluster, logging stuck at loading

### Issue 正文摘录

### Your current environment I have two machine 2*4090, I wanted to runner a model (eg gpt-neox-20b) using vllm on ray cluster, so i follow the documentation by making ray cluster on head ray start --head on node ray start --address= :port I manged to make the cluster so far, when i run simple script for inference: ``` from vllm import LLM llm = LLM("/home/administrator/nlp-deploy/models/gpt-neox-20b/", tensor_parallel_size=2, disable_custom_all_reduce=True, enforce_eager=True) prompt = "GPT-NeoX-20B is" output = llm.generate(prompt) print(output) ``` the model is stuck at loading. nvidia-smi for the head and the node while loading ![image](https://github.com/vllm-project/vllm/assets/83926003/9d4adad6-e165-4e52-a2a5-3e281722586a) logs when running the script ![image](https://github.com/vllm-project/vllm/assets/83926003/57a6d968-fbf7-4f88-be90-895d73141058) versions cuda : 12.4 ray : 2.22 ### 🐛 Describe the bug i tried other solutions mentioned in the issues like `export NCCL_P2P_DISABLE = 1` `disable_custom_all_reduce=True` `enforce_eager=True` and its not solved

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e cluster so far, when i run simple script for inference: ``` from vllm import LLM llm = LLM("/home/administrator/nlp-deploy/models/gpt-neox-20b/", tensor_parallel_size=2, disable_custom_all_reduce=True, enforce_eager=T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: generate(prompt) print(output) ``` the model is stuck at loading. nvidia-smi for the head and the node while loading ![image](https://github.com/vllm-project/vllm/assets/83926003/9d4adad6-e165-4e52-a2a5-3e281722586a) lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: our current environment I have two machine 2*4090, I wanted to runner a model (eg gpt-neox-20b) using vllm on ray cluster, so i follow the documentation by making ray cluster on head ray start --head on node ray start -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
