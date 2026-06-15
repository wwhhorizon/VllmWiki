# vllm-project/vllm#1237: Data parallel inference

| 字段 | 值 |
| --- | --- |
| Issue | [#1237](https://github.com/vllm-project/vllm/issues/1237) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Data parallel inference

### Issue 正文摘录

Is there a recommended way to run data parallel inference (i.e. a copy of the model on each GPU)? It's possible by hacking CUDA_VISIBLE_DEVICES, but I was wondering if there's a cleaner method. ```python def worker(worker_idx): os.environ["CUDA_VISIBLE_DEVICES"] = str(worker_idx) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) if __name__ == "__main__": with multiprocessing.Pool(4) as pool: pool.map(worker, range(4)) ```

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ference (i.e. a copy of the model on each GPU)? It's possible by hacking CUDA_VISIBLE_DEVICES, but I was wondering if there's a cleaner method. ```python def worker(worker_idx): os.environ["CUDA_VISIBLE_DEVICES"] = str(...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ere a recommended way to run data parallel inference (i.e. a copy of the model on each GPU)? It's possible by hacking CUDA_VISIBLE_DEVICES, but I was wondering if there's a cleaner method. ```python def worker(worker_id...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Data parallel inference feature request Is there a recommended way to run data parallel inference (i.e. a copy of the model on each GPU)? It's possible by hacking CUDA_VISIBLE_DEVICES, but I was wondering if there's a c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
