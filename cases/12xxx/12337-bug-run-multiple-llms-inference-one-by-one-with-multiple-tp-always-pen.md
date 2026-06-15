# vllm-project/vllm#12337: [Bug]: Run multiple LLMs inference one by one with multiple TP always pending on the second one in Model list

| 字段 | 值 |
| --- | --- |
| Issue | [#12337](https://github.com/vllm-project/vllm/issues/12337) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Run multiple LLMs inference one by one with multiple TP always pending on the second one in Model list

### Issue 正文摘录

### Your current environment I use my test tool could get from here https://github.com/alexhegit/vLLM_ModelCoverageTest/ The python code copied here, ```python import os import shutil from datetime import datetime import torch import logging from argparse import ArgumentParser import pandas as pd from vllm import LLM, SamplingParams current_date = datetime.now().strftime('%Y%m%d') log_file = f"mct-{current_date}.log" logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') class InferenceEngine: def infer_with_model(self, model_id, gpus): try: if not isinstance(gpus, list) or len(gpus) == 0: logging.error(f" Provided GPUs list is invalid for model {model_id}: {gpus}") return "FAILED" os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(map(str, gpus)) tp = len(gpus) logging.info(f" Inference Model {model_id}, TP {tp}") llm = LLM(model=model_id, tensor_parallel_size=tp, trust_remote_code=True, gpu_memory_utilization=0.95, max_model_len=1024, enforce_eager=True, load_format="dummy" ) prompts = ["The capital of France is"] outputs = llm.generate(prompts, SamplingParams(temperature=0.8, top_p=0.9)) if not outputs or len(outputs) == 0: ra...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: exhegit/vLLM_ModelCoverageTest/ The python code copied here, ```python import os import shutil from datetime import datetime import torch import logging from argparse import ArgumentParser import pandas as pd from vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nference one by one with multiple TP always pending on the second one in Model list bug;stale ### Your current environment I use my test tool could get from here https://github.com/alexhegit/vLLM_ModelCoverageTest/ The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: }") return "FAILED" os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(map(str, gpus)) tp = len(gpus) logging.info(f" Inference Model {model_id}, TP {tp}") llm = LLM(model=model_id, tensor_parallel_
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: SV file or models: {e}") if __name__ == "__main__": main() ``` The reproduce steps are, # Steps: ## Step1: setup a MTP LLM list in csv, e.g. Create the model list in csv file like that, ```bash # cat dev.csv model_id,gp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: logging.info(f" Model cache directory deleted: {cache_dir}") else: logging.warning(f" Model cache directory does not exist: {cache_dir}") except Exception as e: logging.error(f" Error occurred while deleting model cache...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
