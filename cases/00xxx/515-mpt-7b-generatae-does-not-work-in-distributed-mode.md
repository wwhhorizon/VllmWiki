# vllm-project/vllm#515: MPT-7B Generatae does not work in distributed mode

| 字段 | 值 |
| --- | --- |
| Issue | [#515](https://github.com/vllm-project/vllm/issues/515) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> MPT-7B Generatae does not work in distributed mode

### Issue 正文摘录

I tried to inference it the same way the opt-13b example is inferenced, except that my MPT-7b is stored in the local: ``` from vllm import LLM import time llm = LLM(model="/root/mpt-7b", tensor_parallel_size=4, trust_remote_code=True) outputs = llm.generate("San Franciso is a") ``` But got this error: ``` RayTaskError(TypeError) Traceback (most recent call last) Cell In[5], line 2 1 a = time.time() ----> 2 outputs = llm.generate("San Franciso is a") 3 print(outputs) 4 b = time.time() File /opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py:130, in LLM.generate(self, prompts, sampling_params, prompt_token_ids, use_tqdm) 128 token_ids = prompt_token_ids[i] 129 self._add_request(prompt, sampling_params, token_ids) --> 130 return self._run_engine(use_tqdm) File /opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py:150, in LLM._run_engine(self, use_tqdm) 148 outputs: List[RequestOutput] = [] 149 while self.llm_engine.has_unfinished_requests(): --> 150 step_outputs = self.llm_engine.step() 151 for output in step_outputs: 152 if output.finished: File /opt/conda/lib/python3.10/site-packages/vllm/engine/llm_engine.py:245, in LLMEngine.step(self) 242 return [] 244 # Ex...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: = self._run_workers( 246 "execute_model", 247 seq_group_metadata_list=seq_group_metadata_list, 248 blocks_to_swap_in=scheduler_outputs.blocks_to_swap_in, 249 blocks_to_swap_out=scheduler_outputs.blocks_to_swap_out, 250...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: inferenced, except that my MPT-7b is stored in the local: ``` from vllm import LLM import time llm = LLM(model="/root/mpt-7b", tensor_parallel_size=4, trust_remote_code=True) outputs = llm.generate("San Franciso is a")...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: is stored in the local: ``` from vllm import LLM import time llm = LLM(model="/root/mpt-7b", tensor_parallel_size=4, trust_remote_code=True) outputs = llm.generate("San Franciso is a") ``` But got this error: ``` RayTas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m) 128 token_ids = prompt_token_ids[i] 129 self._add_request(prompt, sampling_params, token_ids) --> 130 return self._run_engine(use_tqdm) File /opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py:150, in LLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
