# vllm-project/vllm#4849: [Misc]: Assertion with no scription in vllm with DeepSeekMath 7b model, why, how to fix? 

| 字段 | 值 |
| --- | --- |
| Issue | [#4849](https://github.com/vllm-project/vllm/issues/4849) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | debug |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Assertion with no scription in vllm with DeepSeekMath 7b model, why, how to fix? 

### Issue 正文摘录

### Anything you want to discuss about vllm. I'm working with the DeepSeekMath 7b model to generate synthetic data using Python, but I'm encountering an `AssertionError` with no description alongside warnings related to token length exceeding the model's limit. The relevant portion of my code triggers this issue during a batch operation with `llm.generate(...)`. Here’s the code snippet and the error logs: ```python request_outputs: list[RequestOutput] = gen.llm.generate(batch_prompts, gen.sampling_params) ``` This is part of a larger function that processes datasets, initiated by: ```python lst: list[dict] = gen_data_set_from_ans_str_2_jsonl(gen, path_2_src_dataset, output_path, prompt_template, num_data_gens_per_txt_files=num_data_gens_per_txt_files) ``` Here are the logs indicating the error and warnings: ``` AssertionError: len(all_raw_data)=274 len(all_raw_data)/batch_size = 1/9223372036854775807 = 1 num_batches=1 Processed prompts: 1%|██▌ | 2/274 [00:10 str: """ Generates a synthetic solution to a math problem using a language model. Args: gen (GPT): The language model used to generate the solution. problem (str): The math problem. answer (str): The correct answer to the prob...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: al import VllmGenerator, OpenAIGenerator from evals.utils import get_dtype_for_vllm from evals.inference_eval import VllmGenerator # -- Print print(f'{model=}') print() # -- Get vllm generator prompt_template: str = MAT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: with no scription in vllm with DeepSeekMath 7b model, why, how to fix? stale ### Anything you want to discuss about vllm. I'm working with the DeepSeekMath 7b model to generate synthetic data using Python, but I'm encou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: # TODO -- Batch the data if batched: from evals.utils import batch_data assert batch_size > 0, f'batch_size should be greater than 0 but got: {batch_size=}' all_raw_data: list[dict] = batch_data(all_raw_data, batch_size...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: num_beams: int = None, best_of: int = None, use_beam_search: bool = False, num_similar_data_pts_txt_files: int = 30, # number of problems to use (that were generate from the same mathamatica script) ): """ Gen synthetic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: data)=}') # TODO -- Batch the data if batched: from evals.utils import batch_data assert batch_size > 0, f'batch_size should be greater than 0 but got: {batch_size=}' all_raw_data: list[dict] = batch_data(all_raw_data,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
