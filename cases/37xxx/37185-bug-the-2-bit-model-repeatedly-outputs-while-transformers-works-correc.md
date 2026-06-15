# vllm-project/vllm#37185: [Bug]: The 2-bit model repeatedly outputs !!!!, while Transformers works correctly.

| 字段 | 值 |
| --- | --- |
| Issue | [#37185](https://github.com/vllm-project/vllm/issues/37185) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The 2-bit model repeatedly outputs !!!!, while Transformers works correctly.

### Issue 正文摘录

### Your current environment latest vllm ### 🐛 Describe the bug # VLLM ~~~bash vllm serve OPEA/Qwen2.5-72B-Instruct-int2-sym-inc --max_model_len 512 ~~~ ~~~bash curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d ' { "model": "OPEA/Qwen2.5-72B-Instruct-int2-sym-inc", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "There is a girl who likes adventure,"} ] } ' ~~~ **vllm result** "id":"chatcmpl-a827e041175eb3ca","object":"chat.completion","created":1773660131,"model":"OPEA/Qwen2.5-72B-Instruct-int2-sym-inc","choices":[{"index":0,"message":{"role":"assistant","content":"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","refusal":null,"annotations":null,"audio":null...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _ids":null,"kv_transfer_params":null} # Transformers from transformers import AutoModelForCausalLM,AutoTokenizer quantized_model_dir = "OPEA/Qwen2.5-72B-Instruct-int2-sym-inc" tokenizer = AutoTokenizer.from_pretrained(q...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ransformers from transformers import AutoModelForCausalLM,AutoTokenizer quantized_model_dir = "OPEA/Qwen2.5-72B-Instruct-int2-sym-inc" tokenizer = AutoTokenizer.from_pretrained(quantized_model_dir) model = AutoModelForC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The 2-bit model repeatedly outputs !!!!, while Transformers works correctly. bug ### Your current environment latest vllm ### 🐛 Describe the bug # VLLM ~~~bash vllm serve OPEA/Qwen2.5-72B-Instruct-int2-sym-inc --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) model_inputs = tokenizer([text], return_tensors="pt").to(model.device) generated_ids = model.generate( model_inputs.input...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
