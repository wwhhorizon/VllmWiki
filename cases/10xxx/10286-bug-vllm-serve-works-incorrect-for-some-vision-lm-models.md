# vllm-project/vllm#10286: [Bug]: vllm serve works incorrect for (some) Vision LM models 

| 字段 | 值 |
| --- | --- |
| Issue | [#10286](https://github.com/vllm-project/vllm/issues/10286) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;nondeterministic |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve works incorrect for (some) Vision LM models 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running a Vision LM model `llava-hf/llava-1.5-13b-hf` via `vllm serve`, and it outputs weird outputs: [official script from vllm examples](https://github.com/vllm-project/vllm/blob/3945c82346dae3129213607663bfd17edd905fef/examples/openai_chat_completion_client_for_multimodal.py#L64) with somewhat "fixed" `top_p` for better determinism outputs only '\n' tokens: ``` image_url = "https://wallpapers.com/images/featured/high-resolution-gfinds1akzwf6vcq.jpg" chat_completion_from_url = client.chat.completions.create( messages=[{ "role": "user", "content": [ { "type": "text", "text": "hey" }, { "type": "image_url", "image_url": { "url": image_url }, }, ], }], model="llava-hf/llava-1.5-13b-hf", max_tokens=32, top_p=0.1 ) result = chat_completion_from_url.choices[0].message.content print("Chat completion output from image url:", result) # This outputs the '\n' token 32 times. ``` I launch the vllm server according to[ this official script](https://github.com/vllm-project/vllm/blob/3945c82346dae3129213607663bfd17edd905fef/examples/openai_chat_completion_client_for_multimodal.py#L7): ``` vllm serve ll...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm serve works incorrect for (some) Vision LM models bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running a Vision LM model `llava-hf/llava-1.5-13b-hf` via `v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: f/llava-1.5-13b-hf` via `vllm serve`, and it outputs weird outputs: [official script from vllm examples](https://github.com/vllm-project/vllm/blob/3945c82346dae3129213607663bfd17edd905fef/examples/openai_chat_completion...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ng_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf;nondeterministic env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: for_multimodal.py#L64) with somewhat "fixed" `top_p` for better determinism outputs only '\n' tokens: ``` image_url = "https://wallpapers.com/images/featured/high-resolution-gfinds1akzwf6vcq.jpg" chat_completion_from_ur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None), prompt_token_ids: [1, 3148, 1001, 29901, 29871, 32000, 29871, 13, 354, 29891, 13, 22933, 9047, 13566, 2990...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
