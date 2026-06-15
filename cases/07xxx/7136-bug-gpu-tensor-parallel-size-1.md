# vllm-project/vllm#7136: [Bug]: 单gpu没有任何反应（设置tensor_parallel_size=1模型加载失败）

| 字段 | 值 |
| --- | --- |
| Issue | [#7136](https://github.com/vllm-project/vllm/issues/7136) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 单gpu没有任何反应（设置tensor_parallel_size=1模型加载失败）

### Issue 正文摘录

### Your current environment 问题 ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer import torch # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained('/ProjectRoot/long_content_LLM/qwen/Qwen2-1___5B-Instruct') texts = [] # Prepare your prompts # 定义批量数据 prompts = [ "宪法规定的公民法律义务有", "属于专门人民法院的是", "无效婚姻的种类包括", "刑事案件定义", "税收法律制度", ] for prompt in prompts: messages = [ {"role": "user", "content": prompt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) texts.append(text) sampling_params = SamplingParams(temperature=0.1, top_p=0.5, max_tokens=4096) path = '/ProjectRoot/long_content_LLM/qwen/Qwen2-1___5B-Instruct' llm = LLM(model=path, trust_remote_code=True, tokenizer_mode="auto", tensor_parallel_size=2, dtype=torch.float16) outputs = llm.generate(texts, sampling_params) # 输出结果 for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` 上面这段代码执行没问题，但是当我把tensor_parallel_size从2改成1希望在单卡上面部署离线推理，执行到 ```python llm = LLM(model=path, trust_remote_code=True, tokenizer_mode="auto", tens...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: , trust_remote_code=True, tokenizer_mode="auto", tensor_parallel_size=2, dtype=torch.float16) outputs = llm.generate(texts, sampling_params) # 输出结果 for output in outputs: prompt = output.prompt generated_text = output.o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tokenizer = AutoTokenizer.from_pretrained('/ProjectRoot/long_content_LLM/qwen/Qwen2-1___5B-Instruct') texts = [] # Prepare your prompts # 定义批量数据 prompts = [ "宪法规定的公民法律义务有", "属于专门人民法院的是", "无效婚姻的种类包括", "刑事案件定义", "税收法律制度",...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), seed=0, served_model_name=/ProjectRoot/long_content_LLM/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: our current environment 问题 ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer import torch # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained('...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: xt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) texts.append(text) sampling_params = SamplingParams(temperature=0.1, top_p=0.5, max_tokens=4096) path = '/ProjectRoot/long_conte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
