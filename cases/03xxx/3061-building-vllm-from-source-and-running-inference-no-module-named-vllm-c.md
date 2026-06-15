# vllm-project/vllm#3061: Building VLLM from source and running inference: No module named 'vllm._C'

| 字段 | 值 |
| --- | --- |
| Issue | [#3061](https://github.com/vllm-project/vllm/issues/3061) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Building VLLM from source and running inference: No module named 'vllm._C'

### Issue 正文摘录

Hi, after building vllm from source, the following error occures when running a multi-gpu inference using a local ray instance: ``` File "vllm/vllm/model_executor/layers/quantization/awq.py", line 6, in from vllm._C import ops ModuleNotFoundError: No module named 'vllm._C' ``` I already checked Issue #1814, which does not help. So there is no additional vllm folder to delete, which could lead to confusion. I run the following to build vllm: ``` export VLLM_USE_PRECOMPILED=false git clone https://github.com/vllm-project/vllm.git cd vllm pip install -e . ``` I run the inference using ``` from langchain_community.llms import VLLM from langchain.chains import LLMChain from langchain.prompts import PromptTemplate llm = VLLM(model=model_name, trust_remote_code=True, # mandatory for hf models max_new_tokens=100, top_k=top_k, top_p=top_p, temperature=temperature, tensor_parallel_size=2) prompt = PromptTemplate(template=template, input_variables=["ques"]) llm_chain = LLMChain(prompt=prompt, llm=llm) llm_chain.run(ques) ``` However, building vllm via pip instead leads to an MPI error when running multi-gpu inference (probably due to version incompatiablity of MPI on my System and the prebui...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Building VLLM from source and running inference: No module named 'vllm._C' stale Hi, after building vllm from source, the following error occures when running a multi-gpu inference using a local ray instance: ``` File "
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g a multi-gpu inference using a local ray instance: ``` File "vllm/vllm/model_executor/layers/quantization/awq.py", line 6, in from vllm._C import ops ModuleNotFoundError: No module named 'vllm._C' ``` I already checked...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e using a local ray instance: ``` File "vllm/vllm/model_executor/layers/quantization/awq.py", line 6, in from vllm._C import ops ModuleNotFoundError: No module named 'vllm._C' ``` I already checked Issue #1814, which do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e that all other processes were killed! ``` Some Specs: - Python 3.10 - CUDA 12.1 - OpenMPI/4.1.4. - Torch 2.1.2 development ci_build;distributed_parallel;model_support;quantization;sampling_logits cuda;operator;quantiz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n. I run the following to build vllm: ``` export VLLM_USE_PRECOMPILED=false git clone https://github.com/vllm-project/vllm.git cd vllm pip install -e . ``` I run the inference using ``` from langchain_community.llms imp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
