# vllm-project/vllm#3195: got completely wrong answer for openchat model with vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#3195](https://github.com/vllm-project/vllm/issues/3195) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> got completely wrong answer for openchat model with vllm

### Issue 正文摘录

I got completely wrong answer for openchat model with vllm inference . Tried multiple times and got completely wrong results： model_name_or_path="../models/openchat-3.5-0106" model = LLM(model=model_name_or_path) ``` while True: try: query = input("\n用户：") except UnicodeDecodeError: print("Detected decoding error at the inputs, please set the terminal encoding to utf-8.", file=sys.stderr) continue query = query.strip() if query == "stop": break if query == "clear": session_id = None os.system(clear_command) sampling_params = SamplingParams(temperature=0.8, top_p=0.95) outputs = model.generate(query,sampling_params) print(f"回答结果:{outputs}") ``` I got right answer for openchat model with transformers inference： ``` model_name_or_path="../models/openchat-3.5-0106" model = AutoModelForCausalLM.from_pretrained( model_name_or_path, device_map="auto", offload_folder="offload", offload_state_dict=True, torch_dtype=torch.float16) tokenizer = AutoTokenizer.from_pretrained(model_name_or_path) model.eval() while True: try: query = input("\n用户：") except UnicodeDecodeError: print("Detected decoding error at the inputs, please set the terminal encoding to utf-8.", file=sys.stderr) continue query...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: o", offload_folder="offload", offload_state_dict=True, torch_dtype=torch.float16) tokenizer = AutoTokenizer.from_pretrained(model_name_or_path) model.eval() while True: try: query = input("\n用户：") except UnicodeDecodeEr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: development frontend_api;model_support;sampling_logits cuda;sampling env_dependency I got completely wrong answer for openchat model with vllm inference . Tried multiple times and got completely wrong results：
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _promt, query) inputs = tokenizer(prompt, return_tensors='pt').to('cuda') with torch.no_grad(): output_ids = model.generate( **inputs, do_sample=True, temperature=0.5, top_k=40, eos_token_id=tokenizer.eos_token_id) resu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: alLM.from_pretrained( model_name_or_path, device_map="auto", offload_folder="offload", offload_state_dict=True, torch_dtype=torch.float16) tokenizer = AutoTokenizer.from_pretrained(model_name_or_path) model.eval() while...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: got completely wrong answer for openchat model with vllm I got completely wrong answer for openchat model with vllm inference . Tried multiple times and got completely wrong results： model_name_or_path="../models/opench...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
