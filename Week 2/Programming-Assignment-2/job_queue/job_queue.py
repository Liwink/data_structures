# python3
import heapq


class Worker:
    def __init__(self, index):
        self.index = index
        self.end_time = 0

    def __gt__(self, w2):
        if self.end_time == w2.end_time:
            return self.index > w2.index
        return self.end_time > w2.end_time

    def __lt__(self, w2):
        if self.end_time == w2.end_time:
            return self.index < w2.index
        return self.end_time < w2.end_time


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.workers = []
        for i in range(self.num_workers):
            self.workers.append(Worker(i))

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        for i in range(len(self.jobs)):
            # if 10 <= i <= 20:
            #     print([w.end_time for w in self.workers])
            #     print(self.workers[0] < self.workers[1])
            #     print(self.workers[0] < self.workers[2])
            #     print('\n')
            # worker = self.workers.pop(0)
            worker = heapq.heappop(self.workers)

            self.assigned_workers[i] = worker.index
            self.start_times[i] = worker.end_time

            worker.end_time += self.jobs[i]
            heapq.heappush(self.workers, worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

