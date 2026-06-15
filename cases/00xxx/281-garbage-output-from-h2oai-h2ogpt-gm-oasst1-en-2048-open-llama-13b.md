# vllm-project/vllm#281: garbage output from h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b

| 字段 | 值 |
| --- | --- |
| Issue | [#281](https://github.com/vllm-project/vllm/issues/281) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> garbage output from h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b

### Issue 正文摘录

Using the simple python script on the "supported-models" page I was able to successfully generate output from `TheBloke/Wizard-Vicuna-13B-Uncensored-HF`, but `h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b` generates garbage. I'm running CUDA 11.7.1 on RHEL 8.4 and an NVIDIA A100-SXM-80GB. Here's the script: ``` import sys from vllm import LLM llm = LLM(model=sys.argv[1]) output = llm.generate("Hello, my name is") print(output) ``` Here's output from TheBloke: ``` prompt='Hello, my name is' text="Bastian Mehl and I'm going to talk about how we can solve" ``` And here's output from h2oai: ``` prompt='Hello, my name is' text='\u0442\u0435 Business up t");ymbol\u7532 _ itsardervesag t beskrevs t \u201c ``` Here's the full output: ``` Loading h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b INFO 06-27 10:46:22 llm_engine.py:59] Initializing an LLM engine with config: model='/tmp/h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 06-27 10:46:22 tokenizer_utils.py:30] Using the LLaMA fast tokenizer in 'hf-internal-testing/llama-tokenizer' to avoid potential protobuf error...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: garbage output from h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b Using the simple python script on the "supported-models" page I was able to successfully generate output from `TheBloke/Wizard-Vicuna-13B-Uncensored-HF`,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: with config: model='/tmp/h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 06-27 10:46:22 tokeniz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h2ogpt-gm-oasst1-en-2048-open-llama-13b` generates garbage. I'm running CUDA 11.7.1 on RHEL 8.4 and an NVIDIA A100-SXM-80GB. Here's the script: ``` import sys from vllm import LLM llm = LLM(model=sys.argv[1]) output = l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: oasst1-en-2048-open-llama-13b', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 06-27 10:46:22 tokenizer_utils.py:30] Using the LLaMA fast toke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 11.7.1 on RHEL 8.4 and an NVIDIA A100-SXM-80GB. Here's the script: ``` import sys from vllm import LLM llm = LLM(model=sys.argv[1]) output = llm.generate("Hello, my name is") print(output) ``` Here's output from TheBlok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
