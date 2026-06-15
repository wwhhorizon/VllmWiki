# vllm-project/vllm#16412: [Bug]: corrupted double-linked list (not small) Aborted

| 字段 | 值 |
| --- | --- |
| Issue | [#16412](https://github.com/vllm-project/vllm/issues/16412) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: corrupted double-linked list (not small) Aborted

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On the server side, I deployed the Qwen2.5-32B-Instruct-GPTQ-Int8 model using vLLM on a machine with 4 A6000 GPUs. On the client side, I access the server concurrently with a concurrency level of 3. Each access involves a prompt of about 30,000 bytes. Initially, everything works fine, but suddenly errors occur, such as: "corrupted double-linked list (not small) Aborted," or other errors like "free()" and so on **client** ``` python async def get_driver_labels_with_LLM(llm_server_url, prompt_template, input_str_groups): prompts = [] prompt = prompt_template.replace("{asr_info_str}", input_str_groups) prompts.append(prompt) time.sleep(0.15) data = {"prompts": prompts, "temperature": temperature, "max_new_tokens": max_new_tokens, "top_p": top_p, "top_k": top_k, "repetition_penalty": repetition_penalty} resp = requests.post(llm_server_url, json=data) if resp.status_code == 200: llm_response = resp.json() # think = llm_response["generated_texts"].split(" ")[0] # result = llm_response["generated_texts"].split(" ")[1] result = llm_response["generated_texts"] else: print(name + f" llm response {str(resp.status_code)}") return result asyn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: corrupted double-linked list (not small) Aborted bug;stale ### Your current environment ### 🐛 Describe the bug On the server side, I deployed the Qwen2.5-32B-Instruct-GPTQ-Int8 model using vLLM on a machine with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: corrupted double-linked list (not small) Aborted bug;stale ### Your current environment ### 🐛 Describe the bug On the server side, I deployed the Qwen2.5-32B-Instruct-GPTQ-Int8 model using vLLM on a machine with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ng=True, disable_custom_all_reduce=True ,quantization="gptq", kv_cache_dtype="fp8_e5m2" ) app.run(host='0.0.0.0', port=8090) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: corrupted double-linked list (not small) Aborted bug;stale ### Your current environment ### 🐛 Describe the bug On the server side, I deployed the Qwen2.5-32B-Instruct-GPTQ-Int8 model using vLLM on a machine with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vironment ### 🐛 Describe the bug On the server side, I deployed the Qwen2.5-32B-Instruct-GPTQ-Int8 model using vLLM on a machine with 4 A6000 GPUs. On the client side, I access the server concurrently with a concurrency...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
