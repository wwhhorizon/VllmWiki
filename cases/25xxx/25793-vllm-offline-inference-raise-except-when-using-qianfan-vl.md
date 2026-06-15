# vllm-project/vllm#25793: VLLM offline inference raise except when using qianfan-vl

| 字段 | 值 |
| --- | --- |
| Issue | [#25793](https://github.com/vllm-project/vllm/issues/25793) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> VLLM offline inference raise except when using qianfan-vl

### Issue 正文摘录

### Your current environment vllm 0.10.2 transformers 4.56.2 ### 🐛 Describe the bug global llm, processor #engine_args llm = LLM( model=./Qianfan-VL-8B", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, enforce_eager=True, gpu_memory_utilization=0.9, hf_overrides={"architectures":["InternVLChatModel"],"model_type":"internvl_chat"} ) # 初始化处理器 processor = AutoProcessor.from_pretrained("./Qianfan-VL-8B", trust_remote_code=True) print("✅ 模型加载完成") def call_local_llm(imgpath,text): pil_image = Image.open(imgpath) messages = [ { "role": "user", "content": [ { "type": "image", "image": pil_image }, { "type": "text", "text": text } ] } ] prompts = processor.apply_chat_template(messages,tokenize=False) sampling_params = SamplingParams( n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, temperature=0, #top_p=request.top_p, #top_k=request.top_k, max_tokens=512, # stop=request.stop or [] ) outputs = llm.generate( { "prompt": prompts, "multi_modal_data": {"image": pil_image}, }, sampling_params=sampling_params, ) print("-" * 50) for o in outputs: generated_text = o.outputs[0].text print(generated_text) print("-" * 50) call_local_llm("./test.jpg","Please recognize all t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s llm = LLM( model=./Qianfan-VL-8B", trust_remote_code=True, dtype="float16", tensor_parallel_size=1, en
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: trust_remote_code=True, dtype="float16", tensor_parallel_size=1, enforce_eager=True, gpu_memory_utilization=0.9,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: VLLM offline inference raise except when using qianfan-vl bug;stale ### Your current environment vllm 0.10.2 transformers 4.56.2 ### 🐛 Describe the bug global llm, processor #engine_args llm = LL
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _memory_utilization=0.9, hf_overrides={"architectures":["InternVLChatModel"],"model_type":"internvl_chat"} ) # 初始化处理器 processor = AutoProcessor.fro
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: prompts = processor.apply_chat_template(messages,tokenize=False) sampling_params = SamplingParams( n=1, best_of=1,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
