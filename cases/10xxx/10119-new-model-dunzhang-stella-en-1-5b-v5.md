# vllm-project/vllm#10119: [New Model]: dunzhang/stella_en_1.5B_v5 

| 字段 | 值 |
| --- | --- |
| Issue | [#10119](https://github.com/vllm-project/vllm/issues/10119) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: dunzhang/stella_en_1.5B_v5 

### Issue 正文摘录

### The model to consider. https://huggingface.co/dunzhang/stella_en_1.5B_v5 last_hidden_state = model(**input_data)[0] in __init__ model: vector_linear = torch.nn.Linear(in_features=model.config.hidden_size, out_features=vector_dim) vector_linear_dict = { k.replace("linear.", ""): v for k, v in torch.load(os.path.join(model_dir, f"{vector_linear_directory}/pytorch_model.bin")).items() } vector_linear.load_state_dict(vector_linear_dict) This model is a qwen2 base model,but in the end, a separate linear layer needs to be loaded。 last_hidden = last_hidden_state.masked_fill(~attention_mask[..., None].bool(), 0.0) query_vectors = last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None] query_vectors = normalize(vector_linear(query_vectors) ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: dunzhang/stella_en_1.5B_v5 new-model;stale ### The model to consider. https://huggingface.co/dunzhang/stella_en_1.5B_v5 last_hidden_state = model(**input_data)[0] in __init__ model: vector_linear = torch.nn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: dunzhang/stella_en_1.5B_v5 new-model;stale ### The model to consider. https://huggingface.co/dunzhang/stella_en_1.5B_v5 last_hidden_state = model(**input_data)[0] in __init__ model: vector_linear = torch.nn...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
