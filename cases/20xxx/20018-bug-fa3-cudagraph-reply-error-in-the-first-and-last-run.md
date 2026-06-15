# vllm-project/vllm#20018: [Bug]: FA3 CudaGraph reply error in the first and last run

| 字段 | 值 |
| --- | --- |
| Issue | [#20018](https://github.com/vllm-project/vllm/issues/20018) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FA3 CudaGraph reply error in the first and last run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use `vllm` to deploy `Qwen/Qwen2.5-1.5B-Instruct` on my machine in the Full CudaGraph mode. I choose Flash Attention3 as my backend and use offline batching to do the test, the following is part of my test code: ```qwen_vllm.py sampling_params = SamplingParams(temperature=0.8, top_p=0.95) comp_config = CompilationConfig(use_cudagraph=True, max_num_seqs=32, full_cuda_graph=True) llm = LLM(model="Qwen/Qwen2.5-1.5B-Instruct", compilation_config=comp_config, ) print("begining to generate for batch 1......") prompts0 = [ "I'm from China", "I'm", "how about", "what about", "I'm", ] outputs0 = llm.generate(prompts0, sampling_params, use_tqdm=True) output_txt = [] for output in outputs0: prompt = output.prompt generated_text = output.outputs[0].text output_txt.append(generated_text) print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` I run this code with `VLLM_FLASH_ATTN_VERSION=3 python qwen_vllm.py` , here are the outputs: ```code outputs Prompt: "I'm from China", Generated text: '_graphics.addition统称为全国统称统称为不同。\n统称为各统' Prompt: "I'm", Generated text: ' trying to load data into a MySQL database, and I need to kno...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: FA3 CudaGraph reply error in the first and last run bug;stale ### Your current environment ### 🐛 Describe the bug When I use `vllm` to deploy `Qwen/Qwen2.5-1.5B-Instruct` on my machine in the Full CudaGraph mode....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ted text: {generated_text!r}") ``` I run this code with `VLLM_FLASH_ATTN_VERSION=3 python qwen_vllm.py` , here are the outputs: ```code outputs Prompt: "I'm from China", Generated text: '_graphics.addition统称为全国统称统称为不同。\...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: FA3 CudaGraph reply error in the first and last run bug;stale ### Your current environment ### 🐛 Describe the bug When I use `vllm` to deploy `Qwen/Qwen2.5-1.5B-Instruct` on my machine in the Full CudaGraph mode....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ent environment ### 🐛 Describe the bug When I use `vllm` to deploy `Qwen/Qwen2.5-1.5B-Instruct` on my machine in the Full CudaGraph mode. I choose Flash Attention3 as my backend and use offline batching to do the test,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: FA3 CudaGraph reply error in the first and last run bug;stale ### Your current environment ### 🐛 Describe the bug When I use `vllm` to deploy `Qwen/Qwen2.5-1.5B-Instruct` on my machine in the Full CudaGraph mode....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
