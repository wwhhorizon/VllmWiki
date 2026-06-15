# vllm-project/vllm#7717: [Doc]: AutoAWQ quantization example fails

| 字段 | 值 |
| --- | --- |
| Issue | [#7717](https://github.com/vllm-project/vllm/issues/7717) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: AutoAWQ quantization example fails

### Issue 正文摘录

### 📚 The doc issue The quantization example at https://docs.vllm.ai/en/latest/quantization/auto_awq.html can't be run - it looks like AWQ is looking for safetensors files and https://huggingface.co/lmsys/vicuna-7b-v1.5/tree/main doesn't have them. ``` return model_class.from_pretrained( File "/env/lib/conda/stas-inference/lib/python3.10/site-packages/transformers/modeling_utils.py", line 3477, in from_pretrained raise EnvironmentError( OSError: Error no file named model.safetensors found in directory /data/huggingface/hub/models--lmsys--vicuna-7b-v1.5/snapshots/3321f76e3f527bd14065daf69dad9344000a201d. ``` `autoawq=0.2.6` ### Suggest a potential alternative/fix I tried another model that has .safetensors files but then it fails with: ``` File "/env/lib/conda/stas-inference/lib/python3.10/site-packages/datasets/data_files.py", line 332, in resolve_pattern fs, _, _ = get_fs_token_paths(pattern, storage_options=storage_options) File "/env/lib/conda/stas-inference/lib/python3.10/site-packages/fsspec/core.py", line 681, in get_fs_token_paths paths = [f for f in sorted(fs.glob(paths)) if not fs.isdir(f)] File "/env/lib/conda/stas-inference/lib/python3.10/site-packages/huggingface_hub/h...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: be run - it looks like AWQ is looking for safetensors files and https://huggingface.co/lmsys/vicuna-7b-v1.5/tree/main doesn't have them. ``` return model_class.from_pretrained( File "/env/lib/conda/stas-inference/lib/py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cal and broken at the source. edit: I think the issue is the `datasets` version - I'm able to run this version https://github.com/casper-hansen/AutoAWQ/blob/6f14fc7436d9a3fb5fc69299e4eb37db4ee9c891/examples/quantize.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Doc]: AutoAWQ quantization example fails documentation ### 📚 The doc issue The quantization example at https://docs.vllm.ai/en/latest/quantization/auto_awq.html can't be run - it looks like AWQ is looking for safetenso...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 613, in glob pattern = glob_translate(path + ("/" if ends_with_sep else "")) File "/env/lib/conda/stas-inference/lib/python3.10/site-packages/fsspec/utils.py", line 732, in glob_translate raise ValueError( ValueError: I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: # 📚 The doc issue The quantization example at https://docs.vllm.ai/en/latest/quantization/auto_awq.html can't be run - it looks like AWQ is looking for safetensors files and https://huggingface.co/lmsys/vicuna-7b-v1.5/t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
