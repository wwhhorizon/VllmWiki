# vllm-project/vllm#10662: [Usage]: Cannot use xformers with old GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#10662](https://github.com/vllm-project/vllm/issues/10662) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Cannot use xformers with old GPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug xformers of new version not support GPU with capability (7, 0) (too old) report error “No operator found for `memory_efficient_attention_forward` with inputs” how could i run vllm with v100 ??? what should i do next ? ``` pip show xformers Name: xformers Version: 0.0.28.post3 pip show vllm Name: vllm Version: 0.6.4.post1 ```` Code ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) model_path_prefix ='/home/users/.cache/modelscope/hub/' model_name = 'Qwen/Qwen-7B-Chat' llm = LLM(model=model_path_prefix + model_name,trust_remote_code=True) #llm = LLM(model="facebook/opt-125m") #vllm_model = Model(model_path=local_model_dir) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Error ``` [rank0]: File "/home/users/bai/miniconda3/envs/bai/lib/python3.12/site-packages/torch/ut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: odel Input Dumps _No response_ ### 🐛 Describe the bug xformers of new version not support GPU with capability (7, 0) (too old) report error “No operator found for `memory_efficient_attention_forward` with inputs” how co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e_ ### 🐛 Describe the bug xformers of new version not support GPU with capability (7, 0) (too old) report error “No operator found for `memory_efficient_attention_forward` with inputs” how could i run vllm with v100 ???...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pability > (8, 0) but your GPU has capability (7, 0) (too old) [rank0]: `cutlassF-pt` is not supported because: [rank0]: xFormers wasn't build with CUDA support [rank0]:[W1126 14:58:39.595129646 ProcessGroupNCCL.cpp:125...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: te-packages/vllm/worker/worker.py", line 195, in determine_num_available_blocks [rank0]: self.model_runner.profile_run() [rank0]: File "/home/users/bai/miniconda3/envs/bai/lib/python3.12/site-packages/torch/utils/_conte...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e xformers with old GPU usage;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug xformers of new version not support GPU with capability (7, 0) (too old) report error “No opera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
