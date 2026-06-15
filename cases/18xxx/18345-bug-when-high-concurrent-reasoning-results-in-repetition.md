# vllm-project/vllm#18345: [Bug]: When high concurrent reasoning results in repetition！

| 字段 | 值 |
| --- | --- |
| Issue | [#18345](https://github.com/vllm-project/vllm/issues/18345) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When high concurrent reasoning results in repetition！

### Issue 正文摘录

### Your current environment vllm = 0.8.4 ### 🐛 Describe the bug ``` def get_response(data, model_name=local_model_path , version=None, ip="localhost", port=8000): client = OpenAI(base_url=base_ur, api_key="EMPTY") if model_name is None: models = client.models.list() model_name = models.data[0].id completion = client.chat.completions.create( model=model_name, messages=[ {"role": "system", "content": ""}, {"role": "user", "content": data["prompt"]} ], max_tokens=data.get("max_tokens", 6000), temperature=data.get("temperature", 0.6), top_p=data.get("top_p", 0.95), # extra_body={'top_k':20} ) return completion.choices[0].message def run_in_threads(tasks, ip="localhost", port=8000, max_workers=5): results = [] with ThreadPoolExecutor(max_workers=max_workers) as executor: future_to_task = { executor.submit(get_response, task, ip=ip, port=port): task for task in tasks } for future in tqdm(as_completed(future_to_task), total=len(future_to_task), desc="Processing Tasks"): try: result = future.result() results.append(result) except Exception as e: print(f"Error: {e}") return results def read_jsonl(path, batch_size=100): batch = [] cnt = 0 with open(path, "r", encoding="utf-8") as f: for li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: scribe the bug ``` def get_response(data, model_name=local_model_path , version=None, ip="localhost", port=8000): client = OpenAI(base_url=base_ur, api_key="EMPTY") if model_name is None: models = client.models.list() m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r”. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lt in results: f.write(json.dumps(result, ensure_ascii=False) + "\n") ``` With max_workers = 100, the inference output is normal. With all other parameters unchanged and max_workers = 200, there is a repetition of infer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: onment vllm = 0.8.4 ### 🐛 Describe the bug ``` def get_response(data, model_name=local_model_path , version=None, ip="localhost", port=8000): client = OpenAI(base_url=base_ur, api_key="EMPTY") if model_name is None: mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: When high concurrent reasoning results in repetition！ bug;stale ### Your current environment vllm = 0.8.4 ### 🐛 Describe the bug ``` def get_response(data, model_name=local_model_path , version=None, ip="localhos...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
