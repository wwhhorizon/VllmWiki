# vllm-project/vllm#6969: [Bug]: : ERROR 07-31 11:57:33 async_llm_engine.py:658] Engine iteration timed out. This should never happen!

| 字段 | 值 |
| --- | --- |
| Issue | [#6969](https://github.com/vllm-project/vllm/issues/6969) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: : ERROR 07-31 11:57:33 async_llm_engine.py:658] Engine iteration timed out. This should never happen!

### Issue 正文摘录

### Your current environment ```text : ERROR 07-31 11:57:33 async_llm_engine.py:658] Engine iteration timed out. This should never happen!``` ### 🐛 Describe the bug This code not work: ``` sampling_params = SamplingParams(temperature=0.2, max_tokens=1024, stop=[" ", " "], skip_special_tokens=False) while True: try: inp = input(f"{roles[0]}: ") except EOFError: inp = "" if inp == "\\d": print("exit...") break if is_image(inp): images = load_multi_images_maybe(inp) # clear conv history conv.messages = [] print("Updated image, start new chat session.") continue print(f"{roles[1]}: ", end="") if images is not None: # first message inp = f"{DEFAULT_IMAGE_TOKEN} " * len(images) + "\n" + inp if len(images) > 1: inp = convert_image_tags(inp) conv.append_message(conv.roles[0], inp) else: # later messages conv.append_message(conv.roles[0], inp) conv.append_message(conv.roles[1], None) prompt = conv.get_prompt() if args.debug: print(f"prompt_real: {prompt}") if images is not None: inputs = { "prompt": prompt, "multi_modal_data": { "image": images[0] }, } # next don't need it images = None else: inputs = { "prompt": prompt, } results_generator = model.generate(inputs, sampling_params, str(tim...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: engine.py:658] Engine iteration timed out. This should never happen! bug;stale ### Your current environment ```text : ERROR 07-31 11:57:33 async_llm_engine.py:658] Engine iteration timed out. This should never happen!``...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: amplingParams(temperature=0.2, max_tokens=1024, stop=[" ", " "], skip_special_tokens=False) while True: try: inp = input(f"{roles[0]}: ") except EOFError: inp = "" if inp == "\\d": print("exit...") break if
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: temperature=0.2, max_tokens=1024, stop=[" ", " "], skip_special_tokens=False) while True: try: inp = input(f"{roles[0]}: ") except EOFError: inp = "" if inp == "\\d": print("exit...") break if is_image(inp):
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: "prompt": prompt, } results_generator = model.generate(inputs, sampling_params, str(time.monotonic())) outputs = "" async for request_output in results_generator: prompt = request_output.prompt if request_output.finished

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
