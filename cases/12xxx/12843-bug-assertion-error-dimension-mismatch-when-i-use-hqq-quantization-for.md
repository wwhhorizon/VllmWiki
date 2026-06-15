# vllm-project/vllm#12843: [Bug]:Assertion error(dimension mismatch) when I use HQQ quantization for performance test

| 字段 | 值 |
| --- | --- |
| Issue | [#12843](https://github.com/vllm-project/vllm/issues/12843) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Assertion error(dimension mismatch) when I use HQQ quantization for performance test

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use hqq to do the quantization with quant_config : w4A16+groupsize64. When I want to do online service performance test, I got assertion error: " File "/u/zshao3/vllm/vllm/model_executor/layers/linear.py", line 238, in weight_loader assert param.size() == loaded_weight.size()". Below is the detail: My HQQ quantization script: `import torch from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig model_path = "meta-llama/Llama-2-7b-hf" quant_model = "/scratch/bcjw/zshao3/huggingface/meta-llama/Llama-2-7b-hf-w4-64" quant_config = HqqConfig(nbits=4, group_size=64, axis=1) model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, cache_dir='.', device_map="cuda:0", quantization_config=quant_config, low_cpu_mem_usage=True) tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) model.save_pretrained(quant_model) tokenizer.save_pretrained(quant_model)` The instruction I use to use vllm for performance text: `tmux new -s apiserve conda activate milo_vllm python -m vllm.entrypoints.openai.api_server --disable-log-requests --model /scratch/bcjw/zshao3/huggingface/models--mis...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ### 🐛 Describe the bug I use hqq to do the quantization with quant_config : w4A16+groupsize64. When I want to do online service performance test, I got assertion error: " File "/u/zshao3/vllm/vllm/model_executor/layers/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: aded_weight.size()". Below is the detail: My HQQ quantization script: `import torch from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig model_path = "meta-llama/Llama-2-7b-hf" quant_model = "/scratch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]:Assertion error(dimension mismatch) when I use HQQ quantization for performance test bug;stale ### Your current environment ### 🐛 Describe the bug I use hqq to do the quantization with quant_config : w4A16+groupsi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]:Assertion error(dimension mismatch) when I use HQQ quantization for performance test bug;stale ### Your current environment ### 🐛 Describe the bug I use hqq to do the quantization with quant_config : w4A16+groupsi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: dimension mismatch) when I use HQQ quantization for performance test bug;stale ### Your current environment ### 🐛 Describe the bug I use hqq to do the quantization with quant_config : w4A16+groupsize64. When I want to d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
