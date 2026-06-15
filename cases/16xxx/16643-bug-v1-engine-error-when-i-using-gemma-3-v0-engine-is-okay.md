# vllm-project/vllm#16643: [Bug]: v1 engine error when I using gemma-3 (v0 engine is okay)

| 字段 | 值 |
| --- | --- |
| Issue | [#16643](https://github.com/vllm-project/vllm/issues/16643) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v1 engine error when I using gemma-3 (v0 engine is okay)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug code) model_path = "gaunernst/gemma-3-4b-it-qat-compressed-tensors" token_txt = AutoTokenizer.from_pretrained(model_path,trust_remote_code=True, use_fast=True) proc_txt = AutoProcessor.from_pretrained(model_path,trust_remote_code=True, use_fast=True) # 0.25 quantization="bitsandbytes", dtype="bfloat16", dtype="bfloat16" , max_num_batched_tokens=4096 , load_format="bitsandbytes" model_txt = AsyncLLMEngine.from_engine_args(AsyncEngineArgs(model=model_path, gpu_memory_utilization=0.4, dtype="auto", max_num_seqs=8, max_num_batched_tokens=4096, max_model_len=4096)) ----- @app.post("/v1/txt2chat", summary="문장 기반의 chatgpt 스타일 구현 / batch ") async def txt2chat(chat : Chat): # gen or med print(chat) return StreamingResponse(stream_token(chat,None, False), media_type="text/plain") --- async def stream_token(chat : Chat, img_path, isStream=True): if chat.rag is not None and len(chat.rag) > 10: chat.type= f"{chat.type}\n그리고, 다음 내용을 참고하여 대답을 하되 잘 모르는 내용이면 모른다고 솔직하게 대답하세요.\ncontext\n{chat.rag}" if img_path != None: print('image call',img_path) prompt = proc_txt.apply_chat_template([ {"role": "system", "content" : [{ "type":"text", "text": f"{ch...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: from_pretrained(model_path,trust_remote_code=True, use_fast=True) # 0.25 quantization="bitsandbytes", dtype="bfloat16", dtype="bfloat16" , max_num_batched_tokens=4096 , load_format="bitsandbytes" model_txt = AsyncLLMEng...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: v1 engine error when I using gemma-3 (v0 engine is okay) bug;stale ### Your current environment ### 🐛 Describe the bug code) model_path = "gaunernst/gemma-3-4b-it-qat-compressed-tensors" token_txt = AutoTokenizer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: v1 engine error when I using gemma-3 (v0 engine is okay) bug;stale ### Your current environment ### 🐛 Describe the bug code) model_path = "gaunernst/gemma-3-4b-it-qat-compressed-tensors" token_txt = AutoTokenizer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r med print(chat) return StreamingResponse(stream_token(chat,None, False), media_type="text/plain") --- async def stream_token(chat : Chat, img_path, isStream=True): if chat.rag is not None and len(chat.rag) > 10: chat....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
