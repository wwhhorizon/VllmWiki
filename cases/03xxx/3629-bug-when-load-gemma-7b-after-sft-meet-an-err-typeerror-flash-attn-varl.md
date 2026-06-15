# vllm-project/vllm#3629: [Bug]: when load gemma 7b after sft, meet an err: TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'alibi_slopes' 

| 字段 | 值 |
| --- | --- |
| Issue | [#3629](https://github.com/vllm-project/vllm/issues/3629) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when load gemma 7b after sft, meet an err: TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'alibi_slopes' 

### Issue 正文摘录

### Your current environment pip install vllm-main.zip ### 🐛 Describe the bug [2024-03-26,14:27:51][I][1103-__main__-llm_infer_vllm.py:79]- Setting template_type: default [2024-03-26,14:27:51][I][1103-__main__-llm_infer_vllm.py:211]- sft_args: InferArguments(model_hdfs_name='gemma-7B', sft_type='full', template_type='default', ckpt_dir='/mnt/data/user/luca_model/klara/models/unified_ai_platform_sft_white/v20240319002930/train-model', eval_human=False, seed=42, dtype='bf16', ignore_args_error=False, dataset_seed=42, dataset_sample=-1, dataset_test_size=0.01, system='you are a helpful assistant!', max_length=2048, quantization_bit=None, bnb_4bit_comp_dtype=None, bnb_4bit_quant_type='nf4', bnb_4bit_use_double_quant=True, max_new_tokens=1024, do_sample=False, temperature=0.0, top_k=-1, top_p=0.9, skip_prompt=False, data_path={'train_file': [], 'eval_file': [], 'predict_file': ['/local/data/inference_3446/data/predict_6546.txt']}, remote_result_path='/user/tc_ai/data/aip/task/infer/dataset/inference_3446/predict_result', batch_size=8, sub_task_id=3446) [2024-03-26,14:27:51][I][1103-__main__-llm_infer_vllm.py:111]- generation_config: GenerationConfig { "do_sample": true, "eos_token_id":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d keyword argument 'alibi_slopes' bug ### Your current environment pip install vllm-main.zip ### 🐛 Describe the bug [2024-03-26,14:27:51][I][1103-__main__-llm_infer_vllm.py:79]- Setting template_type: default [2024-03-2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: tform_sft_white/v20240319002930/train-model', eval_human=False, seed=42, dtype='bf16', ignore_args_error=False, dataset_seed=42, dataset_sample=-1, dataset_test_size=0.01, system='you are a helpful assistant!', max_leng...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: when load gemma 7b after sft, meet an err: TypeError: flash_attn_varlen_func() got an unexpected keyword argument 'alibi_slopes' bug ### Your current environment pip install vllm-main.zip ### 🐛 Describe the bug [...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: unified_ai_platform_sft_white/v20240319002930/train-model', eval_human=False, seed=42, dtype='bf16', ignore_args_error=False, dataset_seed=42, dataset_sample=-1, dataset_test_size=0.01, system='you are a helpful assista...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: klara/models/unified_ai_platform_sft_white/v20240319002930/train-model', eval_human=False, seed=42, dtype='bf16', ignore_args_error=False, dataset_seed=42, dataset_sample=-1, dataset_test_size=0.01, system='you are a he...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
