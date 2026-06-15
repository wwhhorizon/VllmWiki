# vllm-project/vllm#11865: [Bug]: Mistral's Pixtral error for vllm>=0.6.5 on 4 T4's

| 字段 | 值 |
| --- | --- |
| Issue | [#11865](https://github.com/vllm-project/vllm/issues/11865) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral's Pixtral error for vllm>=0.6.5 on 4 T4's

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20250108-202622.zip](https://github.com/user-attachments/files/18352929/err_execute_model_input_20250108-202622.zip) ### 🐛 Describe the bug I have 4 T4's (on an AWS g4dn.12xl) and I am trying to run Mistral's pixtral model. I have been able to run it no problems for the past couple of months, in docker, with the following parameters: ``` VLLM_RPC_TIMEOUT: 30000 --model pixtral --quantization None --tensor-parallel-size 4 --dtype float16 --config-format mistral --tokenizer-mode mistral --load-format mistral --distributed-executor-backend mp --limit-mm-per-prompt image=4 --max-model-len 35500 --max-num-batched-tokens 55000 --gpu-memory-utilization 0.90 --enforce-eager --scheduling-policy priority ``` It continues to work with vllm 0.6.4. But, in my docker image, when I install vllm 0.6.5, or 0.6.6 or v0.6.6.post1, with the same parameters, I get the error in the attached file (too many characters to add here). (note: I also have an output with `TORCH_LOGS: "+dynamo"` and `TORCHDYNAMO_VERBOSE: 1` if helpful) Again, it is important to note that the exact same configuration works with vllm 0.6.4. Here is a smal...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: I have been able to run it no problems for the past couple of months, in docker, with the following parameters: ``` VLLM_RPC_TIMEOUT: 30000 --model pixtral --quantization None --tensor-parallel-size 4 --dtype float16 --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: or for vllm>=0.6.5 on 4 T4's bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20250108-202622.zip](https://github.com/user-attachments/files/18352929/err_execute_model_input_20250108-20262...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ad.py", line 759, in _create_aot_dispatcher_function compiled_fn, fw_metadata = compiler_fn( ^^^^^^^^^^^^ File "/home/nonroot/.local/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/jit_compile_runtime_wrappe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ode mistral --load-format mistral --distributed-executor-backend mp --limit-mm-per-prompt image=4 --max-model-len 35500 --max-num-batched-tokens 55000 --gpu-memory-utilization 0.90 --enforce-eager --scheduling-policy pr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ers: ``` VLLM_RPC_TIMEOUT: 30000 --model pixtral --quantization None --tensor-parallel-size 4 --dtype float16 --config-format mistral --tokenizer-mode mistral --load-format mistral --distributed-executor-backend mp

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
