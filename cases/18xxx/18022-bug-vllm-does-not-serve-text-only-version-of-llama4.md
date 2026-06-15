# vllm-project/vllm#18022: [Bug]: vLLM does not serve text-only version of Llama4

| 字段 | 值 |
| --- | --- |
| Issue | [#18022](https://github.com/vllm-project/vllm/issues/18022) |
| 状态 | closed |
| 标签 | feature request;stale;llama |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM does not serve text-only version of Llama4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi all! I am trying to serve a text-only version of Llama 4 Scout (17B-16E) using vLLM. This model requires the Llama4ForCausalLM architecture. However, it seems that vLLM currently expects only the multimodal Llama 4. Although the Llama4ForCausalLM class is implemented in vllm/model_executor/models/llama4.py, it is not registered in the _TEXT_GENERATION_MODELS dictionary in vllm/model_executor/models/registry.py. After manually adding an entry for Llama4ForCausalLM, I was able to serve the model successfully. This looks like an oversight or a missing feature, and might be considered a bug. For the reference, the text-only version of Llama4 was loaded and saved with AutoModelForCausalLM with the model config updated accordingly. ``` model_config = AutoConfig.from_pretrained(config["model"]["path"], trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained( config["model"]["path"], attn_implementation=config["model"]["attn_implementation"], torch_dtype="auto", device_map="auto", trust_remote_code=True, token=token, ) tokenizer = AutoTokenizer.from_pretrained(config["model"]["path"]) ``` ``` os.makedirs(path, exist_ok=Tr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM does not serve text-only version of Llama4 feature request;stale;llama ### Your current environment ### 🐛 Describe the bug Hi all! I am trying to serve a text-only version of Llama 4 Scout (17B-16E) using vL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vLLM does not serve text-only version of Llama4 feature request;stale;llama ### Your current environment ### 🐛 Describe the bug Hi all! I am trying to serve a text-only version of Llama 4 Scout (17B-16E) using vL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: vLLM does not serve text-only version of Llama4 feature request;stale;llama ### Your current environment ### 🐛 Describe the bug Hi all! I am trying to serve a text-only version of Llama 4 Scout (17B-16E) using vL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: attn_implementation=config["model"]["attn_implementation"], torch_dtype="auto", device_map="auto", trust_remote_code=True, token=token, ) tokenizer = AutoTokenizer.from_pretrained(config["model"]["path"]) ``` ``` os.mak...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 4 Scout (17B-16E) using vLLM. This model requires the Llama4ForCausalLM architecture. However, it seems that vLLM currently expects only the multimodal Llama 4. Although the Llama4ForCausalLM class is implemented in vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
