# vllm-project/vllm#7669: [Bug]: Mismatch in the number of image tokens and placeholders during batch inference

| 字段 | 值 |
| --- | --- |
| Issue | [#7669](https://github.com/vllm-project/vllm/issues/7669) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;multimodal_vlm |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mismatch in the number of image tokens and placeholders during batch inference

### Issue 正文摘录

### Your current environment ``` Ray v2.23 Python 3.10 vllm 0.5.4 cuda 12.1 ``` ### 🐛 Describe the bug We are attempting to utilize Ray v2.23 for batch inferencing, specifically on multi-modal data, by leveraging llava-next. ``` dataset = ray.data.read_parquet(gcsInputPath, columns=columns) class LLMPredictor: def __init__(self): # Create an LLM. self.llm = LLM(model="/mnt/models", tensor_parallel_size=1) def __call__(self, batch: Dict[str, np.ndarray]) -> Dict[str, list]: try: start_time = time.time() prompts = [{"prompt": prompt, "multi_modal_data": { "image": Image.open(io.BytesIO(base64.b64decode(batch[imageColumnName][i])))}} for i in range(len(batch[imageColumnName]))] predictions = self.llm.generate( prompts, sampling_params=sampling_params) batch["generated_output"] = [preds.outputs[0].text for preds in predictions] end_time = time.time() print(f'Total Inference Time for {len(prompts)} - {end_time - start_time}') except OSError as os_error: print(f"OS error: {os_error}") batch["generated_output"] = ["" for _ in range(len(batch[imageColumnName]))] except Exception as error: print(f"Misc error: {error}") batch["generated_output"] = ["" for _ in range(len(batch[imageColumnNam...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: def __init__(self): # Create an LLM. self.llm = LLM(model="/mnt/models", tensor_parallel_size=1) def __call__(self, batch: Dict[str, np.ndarray]) -> Dict[str, list]: try: start_time = time.time() prompts = [{"p
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: escribe the bug We are attempting to utilize Ray v2.23 for batch inferencing, specifically on multi-modal data, by leveraging llava-next. ``` dataset = ray.data.read_parquet(gcsInputPath, columns=columns) class LLMPredi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mismatch in the number of image tokens and placeholders during batch inference bug;stale ### Your current environment ``` Ray v2.23 Python 3.10 vllm 0.5.4 cuda 12.1 ``` ### 🐛 Describe the bug We are attempting to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n the number of image tokens and placeholders during batch inference bug;stale ### Your current environment ``` Ray v2.23 Python 3.10 vllm 0.5.4 cuda 12.1 ``` ### 🐛 Describe the bug We are attempting to utilize Ray v2.2...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Mismatch in the number of image tokens and placeholders during batch inference bug;stale ### Your current environment ``` Ray v2.23 Python 3.10 vllm 0.5.4 cuda 12.1 ``` ### 🐛 Describe the bug We are attempting to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
