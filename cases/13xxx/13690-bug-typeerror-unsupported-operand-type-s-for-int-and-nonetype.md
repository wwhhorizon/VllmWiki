# vllm-project/vllm#13690: [Bug]: TypeError: unsupported operand type(s) for //: 'int' and 'NoneType'

| 字段 | 值 |
| --- | --- |
| Issue | [#13690](https://github.com/vllm-project/vllm/issues/13690) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: unsupported operand type(s) for //: 'int' and 'NoneType'

### Issue 正文摘录

### Your current environment vllm 0.7.2 export VLLM_IMAGE_FETCH_TIMEOUT=100 export VLLM_ENGINE_ITERATION_TIMEOUT_S=600 export CUDA_VISIBLE_DEVICES=6,7 model=/llava-1.5-7b-hf max_model_len=32768 sed -i "s/\"max_position_embeddings\": .*$/\"max_position_embeddings\": ${max_model_len},/g" ${model}/config.json python -m vllm.entrypoints.openai.api_server \ --model=${model} \ --host=0.0.0.0 \ --port=9999 \ --max-num-seqs=256 \ --max-model-len=${max_model_len} \ --chat-template /vllm-gpu-0.6.3.post1/examples/template_llava.jinja \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --served-model-name llava-1.5-7b-hf \ --gpu-memory-utilization=0.95 \ --trust-remote-code \ --enforce-eager ### 🐛 Describe the bug Process SpawnProcess-1: Traceback (most recent call last): File "/root/anaconda3/envs/py310/lib/python3.10/site-packages/vllm/inputs/registry.py", line 180, in call_hf_processor return hf_processor(**data, **merged_kwargs, return_tensors="pt") File "/root/anaconda3/envs/py310/lib/python3.10/site-packages/transformers/models/llava/processing_llava.py", line 160, in __call__ num_image_tokens = (height // self.patch_size) * ( TypeError: unsupported operand type(s) for //: 'int' and 'NoneTy...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rt VLLM_ENGINE_ITERATION_TIMEOUT_S=600 export CUDA_VISIBLE_DEVICES=6,7 model=/llava-1.5-7b-hf max_model_len=32768 sed -i "s/\"max_position_embeddings\": .*$/\"max_position_embeddings\": ${max_model_len},/g" ${model}/con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: hat-template /vllm-gpu-0.6.3.post1/examples/template_llava.jinja \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --served-model-name llava-1.5-7b-hf \ --gpu-memory-utilization=0.95 \ --trust-remote-code \ --enforce-eage...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: r.py", line 229, in determine_num_available_blocks self.model_runner.profile_run() File "/root/anaconda3/envs/py310/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*ar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: AGE_FETCH_TIMEOUT=100 export VLLM_ENGINE_ITERATION_TIMEOUT_S=600 export CUDA_VISIBLE_DEVICES=6,7 model=/llava-1.5-7b-hf max_model_len=32768 sed -i "s/\"max_position_embeddings\": .*$/\"max_position_embeddings\": ${max_m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in _initialize_kv_caches self.model_executor.determine_num_available_blocks()) File "/root/anaconda3/envs/py310/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 101, in determine_num_available_blocks r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
