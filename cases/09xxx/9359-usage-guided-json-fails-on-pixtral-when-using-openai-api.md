# vllm-project/vllm#9359: [Usage]: guided_json fails on pixtral when using OpenAI API

| 字段 | 值 |
| --- | --- |
| Issue | [#9359](https://github.com/vllm-project/vllm/issues/9359) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: guided_json fails on pixtral when using OpenAI API

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have OpenAI compatible server running inside docker with the following arguments: `--model mistralai/Pixtral-12B-2409 --dtype bfloat16 --uvicorn-log-level debug --tensor-parallel-size 1 --max-num-seqs 32 --gpu-memory-utilization=.98 --disable-log-stats --tokenizer_pool_size=4 --distributed-executor-backend=ray --tokenizer_mode mistral --limit_mm_per_prompt 'image=4' --max-model-len 16000 ` If I make a request: ```python guided_json = {'properties': {'image_caption': {'title': 'Image Caption', 'type': 'string'}}, 'required': ['image_caption'], 'title': 'Caption', 'type': 'object'} kwargs = dict(max_tokens=512, stream = False, top_p=.9, temperature=.5, model = model_id, guided_json =guided_json, messages=[{"role":"system", "content": "Format response as JSON"}, {"role": "user", "content": [ {"type": "text", "text": "caption the image"}, { "type": "image_url", "image_url": { "url": get_image_url(f), }, }, ], }], ) a = requests.post(url, json= kwargs) ``` I get ` ` . In the vllm logs I also get: ```text WARNING 10-14 20:36:36 chat_utils.py:570] 'add_generation_prompt' is not supported for mistral...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### 🐛 Describe the bug I have OpenAI compatible server running inside docker with the following arguments: `--model mistralai/Pixtral-12B-2409 --dtype bfloat16 --uvicorn-log-level debug --tensor-parallel-size 1 --max-nu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: pixtral when using OpenAI API usage ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have OpenAI compatible server running inside docker with the following arguments: `--model mi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ker with the following arguments: `--model mistralai/Pixtral-12B-2409 --dtype bfloat16 --uvicorn-log-level debug --tensor-parallel-size 1 --max-num-seqs 32 --gpu-memory-utilization=.98 --disable-log-stats --tokenizer_po...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: n=.98 --disable-log-stats --tokenizer_pool_size=4 --distributed-executor-backend=ray --tokenizer_mode mistral --limit_mm_per_prompt 'image=4' --max-model-len 16000 ` If I make a request: ```python guided_json = {'proper...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 72B ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
